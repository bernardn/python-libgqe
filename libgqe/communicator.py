"""
Communication interface abstraction layer

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

import sys
import serial


class Communicator:
    """ Serial communication layer """
    def __init__(self, **kwargs):
        self._device = kwargs['port']
        self.rw_functions = (self.read, self.write)

        try:
            self.interface = serial.Serial(self._device, kwargs['baud_rate'], timeout=1.5)
        except serial.serialutil.SerialException as err:
            print(err)
            sys.exit(1)

    def read(self, response_interpreter):
        """ reader function. expects a response interpreter object """
        # print("read {}".format(response_interpreter))
        if response_interpreter is None:
            return None
        while response_interpreter.parse(self.interface.read(response_interpreter.read_bytes)):
            pass

        return response_interpreter.response

    def write(self, data):
        """writer function"""
        if self.interface.in_waiting:
            # For the protocol is loose and what can differ between versions,
            # we want to know if extra bytes are unexpectedly received. Those bytes are eventually drained out
            buffer = self.interface.read(self.interface.in_waiting)
            print("{} remaining bytes drained from buffer : {}.".format(len(buffer), buffer), file=sys.stderr)
        return self.interface.write(data)
