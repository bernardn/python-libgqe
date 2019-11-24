"""
Abstraction layer for firmware Re 2.00 and above

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
    "Re_2_00",
    "rtc",
    "spectrum",
    "spi"
]

from libgqe.unit.gqemf.re_1_00 import Re_1_00
from libgqe.protocol.GQRFC1701.v2_00 import GETXYZ


class Re_2_00(Re_1_00):
    """Abstraction class for firmware Re 2.16 and above"""
    def __init__(self, *args, **kwargs):
        Re_1_00.__init__(self, *args, **kwargs)
        # print("Initializing protocol GQRFC1701.V2_00 for Re 2.00")

    def cmd_get_xyz(self, *args, **kwargs):
        """Retrieve magnetic field on x, y and z axes"""
        cmd = GETXYZ.GETXYZ(self.rw_functions, *args, **kwargs)
        cmd.send()
        return cmd.response
