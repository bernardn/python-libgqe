"""
GQ-RFC1701 protocol implementation: Command - DSID

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

from libgqe.protocol.GQRFC1701.v2_01 import Protocol


class DSID(Protocol):
    """Undocumented command"""
    ARGUMENTS = None
    RESPONSE_TYPE = Protocol.Response.Bytes(8)

    def _parse_response(self, value):
        res = ''
        for byte in bytearray(value):
            res += "{:0>2X}".format(byte)
        return res
