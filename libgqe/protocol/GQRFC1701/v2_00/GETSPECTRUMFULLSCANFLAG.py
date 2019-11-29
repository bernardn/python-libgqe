"""
GQ-RFC1701 protocol implementation: Command - GETSPECTRUMFULLSCANFLAG

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


class GETSPECTRUMFULLSCANFLAG(Protocol):
    """
        Get scan completed flag from the spectrum analyzer.

        :returns: 2 bytes total (0x00 or 0x01) + 0xAA
            e.g. 0x00 0xAA = not finished
                 0x01 0xAA = finished
            this flag is cleared after a successful <GETBANDDATA>> Call or <RESETBANDDATA>>
    """
    ARGUMENTS = None
    RESPONSE_TYPE = Protocol.Response.Terminator(b'\xaa')

    def _parse_response(self, value):
        if value[0] == 0:
            return False
        if value[0] == 1:
            return True
        raise ValueError("Invalid value: {}".format(value))
