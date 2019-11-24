"""
JSON data formatter

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

from json import dumps
from libgqe.format import Format


class Json(Format):
    """JSON data formatter class"""
    def format(self, data):
        """Formats data to JSON"""
        r = dumps(data, sort_keys=True, indent=4, default=str)
        self.write(r)
        self.write("\n")

    def format_generator(self, data):
        """Formats generator data to JSON"""
        r = []
        for rec in data:
            r.append(rec)
        r = dumps(r, sort_keys=True, indent=4, default=str)
        self.write(r)
