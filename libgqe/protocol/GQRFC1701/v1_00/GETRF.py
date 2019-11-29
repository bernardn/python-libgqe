"""
GQ-RFC1701 protocol implementation: Command - GETRF

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

from libgqe.protocol.GQRFC1701.v1_00 import Protocol


class GETRF(Protocol):
    """
        Returns the max rf power in watts with the max rf frequency it detected
        :argument: WATTS, DBM, DENSITY, 8GTOTALDENSITY, 8GTOTALPEAK in ascii
        :returns: string, e.g. 4 nW(866 MHz)

    """
    ARGUMENTS = [
        Protocol.Argument.List('WATTS', 'DBM', 'DENSITY', '8GTOTALDENSITY', '8GTOTALPEAK')
    ]
    # N.B. Protocol. A bracket isn't really a nice terminator.
    RESPONSE_TYPE = Protocol.Response.Terminator(b')')

    def _parse_response(self, value):
        values = value.split(b' ', 2)
        return values[0].decode(), values[1].decode(), values[2].decode()
