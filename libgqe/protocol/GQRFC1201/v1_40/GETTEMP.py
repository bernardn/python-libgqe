"""
GQ-RFC1201 protocol implementation: Command - GETTEMP

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


class GETTEMP(Protocol):
    """Retrieve the current temperature"""
    ARGUMENTS = None
    RESPONSE_TYPE = Protocol.Response.Bytes(4)

    def _parse_response(self, value):
        if value[3] != ord('\xaa'):
            raise ValueError('Invalid terminator received: {}'.format(value[3]))
        val = value[0] + value[1] / 10
        if value[2]:
            return -val
        return val
