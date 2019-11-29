"""
Formatter abstraction layer

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

from _io import TextIOWrapper


class Format:
    """Formatter abstraction class"""
    def __init__(self, *args, **kwargs):  # pylint: disable=unused-argument
        self.out_file = kwargs['out_file']
        self.out_file_io = None

    def format(self, data):
        """Format data"""
        self.write(data)

    def format_generator(self, data):
        """Format generator data"""
        for rec in data:
            self.write(rec)

    def write(self, data):
        """Write data to IO"""
        if data:
            try:
                _io = self._get_io(type(data))
                if isinstance(_io, TextIOWrapper):
                    _io.write(str(data))
                else:
                    _io.write(data)
            except BrokenPipeError:
                pass

    def _get_io(self, type_data):
        if self.out_file_io:
            return self.out_file_io

        if isinstance(self.out_file, TextIOWrapper):
            self.out_file_io = self.out_file
        elif isinstance(self.out_file, str):
            mode = 'w'
            if type_data in (bytes, bytearray):
                mode += 'b'
            self.out_file_io = open(self.out_file, mode)
            # Todo close that file at some point
        else:
            raise TypeError("Unknown output file object type: {}".format(type(self.out_file)))

        return self.out_file_io

    class NeedsList(ValueError):
        """NeedsListError"""
