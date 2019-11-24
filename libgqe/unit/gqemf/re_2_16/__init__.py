"""
Abstraction layer for firmware Re 2.16 and above

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

from libgqe.unit.gqemf.re_2_00 import Re_2_00
from libgqe.protocol.GQRFC1701.v2_01 import GETRF, DSID

__all__ = [
    "Re_2_16",
    # Modules
    "rtc", "spectrum", "spi"
]


class Re_2_16(Re_2_00):
    """Abstraction class for firmware Re 2.16 and above"""
    def __init__(self, *args, **kwargs):
        Re_2_00.__init__(self, *args, **kwargs)
        # print("Initializing protocol GQRFC1701.V2_01 for Re 2.16")

    def cmd_get_rf(self, measurement='TOTALDENSITY', *args, **kwargs):
        """Retrieves an RF measurement"""
        cmd = GETRF.GETRF(self.rw_functions, *args, **kwargs)
        cmd.send(measurement.upper())
        return cmd.response

    def cmd_get_dsid(self, *args, **kwargs):
        """Undocumented command"""
        cmd = DSID.DSID(self.rw_functions, *args, **kwargs)
        cmd.send()
        return cmd.response
