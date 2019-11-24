"""
GQ-RFC protocols implementation: Command - GETGYRO

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

from libgqe.protocol import Protocol


class GETGYRO(Protocol):
    """ Get gyroscope data """
    ARGUMENTS = None
    RESPONSE_TYPE = Protocol.Response.Terminator(b'\xaa')
    RESPONSE_TYPE.read_bytes = 7

    def _parse_response(self, value):
        return {
            'x': value[0] * 256 + value[1],
            'y': value[2] * 256 + value[3],
            'z': value[4] * 256 + value[5],
        }
