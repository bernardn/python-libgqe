"""
CSV data formatter

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

from libgqe.format.txt import Txt


class Csv(Txt):
    """CSV data formatter class"""
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self.separators = [
            ';',
            '\n',
        ]

    def format(self, data):
        """Formats data to CSV"""
        self._depth += 1
        if self._depth > self._max_depth:
            self._max_depth = self._depth

        if isinstance(data, str):
            self.write(data)
        elif isinstance(data, (list, tuple)):
            for val in data:
                self.format(val)
                self.write(self.separators[0])
            self.write(self.separators[1])
        elif isinstance(data, dict):
            for val in data.values():
                self.format(val)
                self.write(self.separators[0])
            self.write(self.separators[1])
        else:
            self.write(str(data))
        self._depth -= 1

    def format_generator(self, data):
        """Formats generator data to CSV"""
        for rec in data:
            self.write(self.format(rec))
