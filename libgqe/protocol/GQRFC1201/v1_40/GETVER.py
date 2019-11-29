"""
GQ-RFC1201 protocol implementation: Command - GETVER

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

from libgqe.protocol.GQRFC1201.v1_40 import Protocol


class GETVER(Protocol):
    """Get hardware model and version"""
    ARGUMENTS = None
    RESPONSE_TYPE = Protocol.Response.Bytes(14)

    def _parse_response(self, value):
        mod = value[0:7]
        ver = value[7:14]
        return mod.decode(), ver.decode()
