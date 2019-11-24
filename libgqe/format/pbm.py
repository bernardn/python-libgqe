"""
PBM bitmap image formatter

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


class Pbm(Format):
    """PBM Bitmap image formatter class"""
    def __init__(self, *args, width=128, height=64, **kwargs):
        super().__init__(self, *args, **kwargs)
        self.height = height
        self.width = width

    def format(self, data):
        self.write(bytearray("P4\n# {}\n{} {}\n".format('', self.width, self.height), 'ascii'))
        self.write(data)
