"""
GQE unit abstraction layer

Copyright (c) Bernard Nauwelaerts 2019.
All rights reserved

This program is free software; you can redistribute it and/or modify it under the terms of the
GNU General Public License as published by the Free Software Foundation; version 2.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program;
if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.

"""
__all__ = [
    "Unit"
]

import importlib
import time
import operator
from types import GeneratorType
import yaml

from libgqe.communicator import Communicator
from libgqe.protocol import GETVER


class Unit:
    """GQE unit base class"""
    def __init__(self, *args, **kwargs):  # pylint: disable=unused-argument
        self._communicator = Communicator(**kwargs)
        self.rw_functions = self._communicator.rw_functions
        self.kwargs = kwargs
        self.instance = None
        self.protocol = None
        self.model = None
        self.version = None

    def auto_load(self):
        """Autodetect connected unit"""
        def get_version(product_class, firmware_revision):
            mod = importlib.import_module('libgqe.unit.{}'.format(product_class.lower()))
            revs = mod.FIRMWARE_REVISIONS
            if firmware_revision in revs:
                return firmware_revision
            revs.append(firmware_revision)
            revs.sort()
            return mod.FIRMWARE_REVISIONS[operator.indexOf(revs, firmware_revision) - 1]

        model = None
        version = None

        if 'unit' in self.kwargs.keys():
            model = self.kwargs['unit']
            self.model = model

        if 'version' in self.kwargs.keys():
            version = self.kwargs['version']
            self.version = version

        if not model or not version:
            cmd = GETVER.GETVER(self.rw_functions)
            cmd.send()
            model = cmd.response[0]
            version = cmd.response[1]

        # Load Model
        classes = []

        model = model.replace('_', '')
        model = model.replace('-', '')
        model = model.replace('+', 'Plus')
        cmodel = model.rstrip('Plus')
        cmodel = cmodel.rstrip('0123456789')
        try:
            mod_unit = importlib.import_module('libgqe.unit.{}.{}'.format(cmodel.lower(), model.lower()))
        except ModuleNotFoundError:
            raise Unit.UnknownUnitModelError(self.kwargs['unit'])

        # Load Protocol
        version = version.replace('.', '_')
        version = version.replace(' ', '_')
        version = get_version(cmodel, version)
        mod_version = importlib.import_module('libgqe.unit.{}.{}'.format(cmodel.lower(), version.lower()))

        classes.append(getattr(mod_version, version.capitalize()))
        classes.append(getattr(mod_unit, model))
        for module in classes[len(classes) - 1].MODULES:
            mod = importlib.import_module('libgqe.unit.{}.{}.{}'.format(
                cmodel.lower(),
                version.lower(),
                module.lower()
            ))
            classes.append(getattr(mod, module))

        def class_factory(*parent_classes):
            # pylint: disable=too-few-public-methods
            class SuperClass(*parent_classes):
                """Superclass factory"""
                def __init__(self, **kwargs):
                    for parent_class in parent_classes:
                        # print(parent_class) # todo if verbose
                        parent_class.__init__(self, **kwargs)
            return SuperClass

        superclass = class_factory(*classes)
        self.instance = superclass(**self.kwargs)
        return self.instance

    @staticmethod
    def command(name, protocol, version, *args, **kwargs):
        """Send a named command to the unit"""
        try:
            module = importlib.import_module('libgqe.protocol.{}.{}.{}'.format(protocol, version, name))
            attr = getattr(module, name)
            return attr(*args, **kwargs)
        except ImportError:
            return None

    @property
    def actions(self):
        """Dictionary of actions available to the current unit and their description"""
        res = {}
        for met in [f for f in dir(self) if f.startswith("cmd_") and callable(getattr(self, f))]:
            doc = getattr(self, met).__doc__
            arg = getattr(self, met).__defaults__
            if arg:
                arg = len(arg)
            else:
                arg = 0
            res[met.lstrip("cmd_").replace('_', '-')] = (arg, doc)
        return res

    def action(self, name='', *args, **kwargs):
        """Execute a named action with given args"""
        try:
            met = getattr(self, "cmd_{}".format(name.replace('-', '_')))
        except AttributeError:
            raise Unit.UnavailableActionError

        res = met(*args, **kwargs)

        format_r = importlib.import_module('libgqe.format.{}'.format(kwargs['format']))
        format_r = getattr(format_r, kwargs['format'].capitalize())
        format_r = format_r(out_file=kwargs['out_file'])
        if isinstance(res, (list, tuple)):
            res = format_r.format(res)
        elif isinstance(res, GeneratorType):
            res = format_r.format_generator(res)
        else:
            res = format_r.format(res)
        format_r.write(res)

        return res

    @staticmethod
    def cmd_wait(time_to_wait=0, *args, **kwargs):   # pylint: disable=unused-argument
        """Wait for the specified number of seconds to elapse"""
        time.sleep(float(time_to_wait))

    def cmd_play(self, file=None, *args, **kwargs):  # pylint: disable=unused-argument
        """Play a list of commands described in specified YAML file"""
        with open(file) as fil:
            doc = yaml.load(fil.read())
        for action in doc['playbook']['actions']:
            if isinstance(action, str):
                action = {action: None}
            for cmd, arg in action.items():
                print("{}: {}".format(cmd, arg))
                args = []
                if isinstance(arg, dict):
                    # It is indeed subscribable, since it's a dict instance.
                    # pylint: disable=unsubscriptable-object
                    if 'args' in arg.keys():
                        args.append(arg['args'])
                    if 'out_file' in arg.keys():
                        kwargs['out_file'] = arg['out_file']
                    if 'format' in arg.keys():
                        kwargs['format'] = arg['format']
                elif isinstance(arg, bool):
                    args.append(arg.real)
                elif isinstance(arg, (str, int, float)):
                    args.append(arg)
                elif not arg:
                    pass
                else:
                    print("Unknown value type : {}".format(type(arg)))

                try:
                    self.action(cmd, *args, **kwargs)
                except Unit.UnavailableActionError:
                    print("Action '{}' unavailable to the unit".format(cmd))

    class UnavailableActionError(BaseException):
        """Risen when specified action is unavailable"""

    class UnknownUnitModelError(BaseException):
        """Risen when unit model is unknown to this software"""
