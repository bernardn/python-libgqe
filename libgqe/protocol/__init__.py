"""
GQ-RFCxxx protocols implementation

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

import time
import datetime

__all__ = [
    # Parent Classes
    "Protocol",
    # Commands
    "CFGUPDATE", "ECFG", "FACTORYRESET", "GETDATETIME", "GETGYRO", "GETSERIAL", "GETVER", "KEY", "POWER", "REBOOT",
    "SETDATEDD", "SETTIMESS", "SETTIMEMM", "SETTIMEHH", "SETDATEYY", "SETDATEMM", "SETDATETIME", "SPIR"
]


class Protocol:
    """ Base class for Commands to be sent to the unit. """
    ARGUMENTS = []
    RESPONSE_TYPE = None

    def __init__(self, rw_connectors, *args, out_format=None, **kwargs):  # pylint: disable=unused-argument
        self.response = ''
        self.format = out_format
        self.reader = rw_connectors[0]
        self.writer = rw_connectors[1]
        self._args = []
        self.read_bytes = 0
        self.unit = None

    def build(self, args=()):
        """ Command's binary representation """
        cmd = bytearray("<{}".format(self.__class__.__name__), 'ascii')
        for arg in args:
            if isinstance(arg, str):
                for char in arg:
                    cmd.append(ord(char))
            elif isinstance(arg, int):
                cmd.append(arg % 256)  # Restrained to byte argument value
            else:
                print("error")
                raise ValueError("Invalid argument data type {} for {}".format(type(arg), arg))
        cmd.append(ord('>'))
        cmd.append(ord('>'))
        return cmd

    def send(self, *args):
        """ Send the command to the unit. """
        if self.ARGUMENTS and len(self.ARGUMENTS) > 0:
            self._args = []
            for i in range(0, len(self.ARGUMENTS)):
                self._args.append(self.ARGUMENTS[i].parse(args[i]))

        if self.RESPONSE_TYPE:
            self.RESPONSE_TYPE.reset()

        self.writer(self.build(self._args))

        if self.RESPONSE_TYPE:
            try:
                if self.format and self.format == 'raw':
                    self.response = self.reader(self.RESPONSE_TYPE)
                else:
                    # self.response_raw = self.reader(self.RESPONSE_HANDLER(self.RESPONSE_HANDLER_ARGS))
                    self.response = self._parse_response(self.reader(self.RESPONSE_TYPE))

            except Protocol.Response.EmptyError:
                self.response = None
                raise
        else:
            self.response = ""
            time.sleep(0.1)  # Todo Not sure it's best here to compensate for device's time to process

        return self.response

    @staticmethod
    def _parse_response(value):
        """ Default """
        return value

    @staticmethod
    def _parse_timestamp(value):
        r = []
        for b in bytearray(value[:6]):
            r.append(int("{:0>2d}".format(b)))
        dt = datetime.datetime.now()
        r[0] += 100 * int(dt.year / 100)
        dt = datetime.datetime(*r)
        return dt

    def __str__(self):
        args = ''
        for a in self._args:
            args = args + "\\x{:0>2x}".format(a % 256)
        return '<{}{}>>'.format(self.__class__.__name__, args)

    class Argument:
        """ Command's arguments expected types.  """
        # pylint: disable=too-few-public-methods
        class Binary:
            """ Binary argument type. The first constructor argument represents the binary 0, the second one, the 1."""
            values = (
                ('0', 'off', 'no', 'false', 'disable', 'disabled'),  # 0
                ('1', 'on', 'yes', 'true', 'enable', 'enabled')      # 1
            )

            def __init__(self, out_0=0, out_1=1):
                self._output = (out_0, out_1)
                self.value = None

            def parse(self, value):
                """Parse binary argument value"""
                r = None
                if isinstance(value, bool):
                    if not value:
                        r = 0
                    else:
                        r = 1
                elif isinstance(value, int):
                    if value == 0:
                        r = 0
                    elif value == 1:
                        r = 1
                elif isinstance(value, str):
                    if value.lower() in self.values[0]:
                        r = 0
                    elif value.lower() in self.values[1]:
                        r = 1

                if r is not None:
                    self.value = self._output[r]
                else:
                    raise ValueError("Invalid boolean value: {}".format(value))

                # print("bin ret val {}".format(self.value))
                return self.value

        class Numeric:
            """Numeric argument type. First argument is minimal value, second the maximal. If arguments are a string,
            the value will be outputed as ascii, if not as binary"""
            def __init__(self, minimum, maximum):
                self._min_max = (minimum, maximum)
                self.value = None

            def parse(self, value):
                """Parse numeric argument value"""
                r = 0
                if isinstance(value, bool):
                    if not value:
                        r = 0
                    else:
                        r = 1
                elif isinstance(value, int):
                    r = value
                elif isinstance(value, str):
                    r = int(value)

                min_val = self._min_max[0]
                max_val = self._min_max[1]

                min_int = int(min_val)
                max_int = int(max_val)

                if r < min_int or r > max_int:
                    raise ValueError("Argument value must be comprised between {} and {}".format(min_int, max_int))

                if isinstance(min_val, str):
                    r = str(r)
                self.value = r
                return self.value

        class List:
            """Value must be present in the constructor list"""
            def __init__(self, *expected_values):
                self._expected_values = expected_values
                self.value = None

            def parse(self, value):
                """Check if argument value is present un list"""
                if value not in self._expected_values:
                    raise ValueError("Invalid argument value: {} not in {}".format(value, self._expected_values))
                self.value = value
                return self.value

        class Ascii:
            """Argument value is an ASCII string. Constructor arg is max string length"""
            def __init__(self, max_chars=1):
                self._max_chars = max_chars
                self.value = None

            def parse(self, value):
                """Parse ASCII argument value"""
                if len(value) > self._max_chars:
                    raise ValueError("String too long")
                try:
                    return value.encode('ascii')
                except UnicodeEncodeError:
                    raise ValueError("String must be ASCII")

    class Response:
        """ These classes define how a given command's response has to be interpreted. """
        # pylint: disable=too-few-public-methods
        class Byte:
            """ The byte given in constructor's first argument is the one that's expected to be received. """
            def __init__(self, expected_byte):
                self.expected_byte = expected_byte
                self.read_bytes = 1
                self.response = b''

            def reset(self):
                """Reset response state"""
                self.response = b''

            def parse(self, data):
                """Parse byte response data"""
                self.response = data
                if self.expected_byte and data and ord(self.expected_byte) == ord(data):
                    return None
                if not self.expected_byte:
                    return ''
                if data:
                    raise Protocol.Response.UnexpectedValueError("{} vs. {}".format(data, self.expected_byte))
                raise Protocol.Response.EmptyError("Byte 0x{:02X} expected but none received".format(
                    ord(self.expected_byte)
                    ))

            def __repr__(self):
                return "Byte(0x{:02X})".format(ord(self.expected_byte))

        class Bytes:
            """ The byte given in constructor's first argument is the number of bytes to be received. """
            def __init__(self, num_bytes=1):
                self.read_bytes = num_bytes
                self.response = b''

            def reset(self):
                """Reset response state"""
                self.response = b''

            def parse(self, data):
                """Parse bytes response data"""
                self.response += data
                if len(self.response) == self.read_bytes:
                    return None
                if len(data) == 0:
                    raise Protocol.Response.EmptyError

                raise Protocol.Response.SizeMismatchError(
                    "data size mismatch: received {} vs. {} expected. response: {}".format(
                        len(self.response),
                        self.read_bytes,
                        self.response
                    )
                )

            def __repr__(self):
                return "Bytes(0x{:02X})".format(self.read_bytes)

        class Terminator:
            """ The terminator byte given in constructor's first argument will complete the reading loop. """
            def __init__(self, terminator_bytes):
                self._terminator = terminator_bytes
                if terminator_bytes:
                    self.read_bytes = len(terminator_bytes)
                else:
                    self.read_bytes = 1
                self.response = b''

            def reset(self):
                """Reset response state"""
                self.response = b''

            def parse(self, data):
                """ Stack up incoming bytes until terminator arrives. """
                resp_data = self.response + data
                if not data:
                    if self.response and self._terminator:
                        raise Protocol.Response.TerminatorNotFoundError("{}".format(self))
                    if not self.response and self._terminator:
                        raise Protocol.Response.EmptyError
                    return None
                if self._terminator and resp_data.endswith(self._terminator):
                    self.response += data
                    return None

                self.response += data
                return data

            def __repr__(self):
                return "Terminator({})='{}'".format(self._terminator, self.response)

        class SizeMismatchError(ValueError):
            """ Raised when the size of received data mismatches expected size."""

        class EmptyError(SizeMismatchError):
            """ Raised when no data has been received in response."""

        class UnexpectedValueError(ValueError):
            """ Raised when unexpected data has been received in response."""

        class TerminatorNotFoundError(ValueError):
            """ Raised when the specified terminator hasn't been found in response."""
