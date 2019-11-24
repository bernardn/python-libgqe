"""
Plain Text data formatter

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

from libgqe.format import Format


class Txt(Format):
    """Text data formatter class"""
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self._depth = -1
        self._max_depth = 0
        self.separators = [
            ' ',
            '\n',
            '\n',
        ]

    def format(self, data):
        self._depth += 1
        if self._depth > self._max_depth:
            self._max_depth = self._depth
        if data:
            sepid = self._max_depth - self._depth

            if isinstance(data, (tuple, list)):
                for val in data:
                    self.format(val)
                    self.write(self.separators[sepid])
                self.write(self.separators[sepid+1])
            elif isinstance(data, dict):
                max_len = 0
                for key in data.keys():
                    if len(key) > max_len:
                        max_len = len(key)
                for key, val in data.items():
                    self.write("{}:{}".format(key, ' ' * (max_len - len(key) + 1)))
                    self.format(val)
                    self.write(self.separators[sepid+1])
            else:
                self.write(str(data))
        elif isinstance(data, (int, float)):
            self.write(str(data))
        #else:
        #    self.write(type(data))
        self._depth -= 1

    def format_generator(self, data):
        self._depth += 1
        for rec in data:
            self.format(rec)
        self._depth -= 1
