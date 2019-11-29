"""
GQ-RFC1701 protocol implementation: Command - GETXYZ

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


class GETXYZ(Protocol):
    """ Get the x, y, and z EMF values """
    ARGUMENTS = None
    RESPONSE_TYPE = Protocol.Response.Terminator(b'mG')

    def _parse_response(self, value):
        vaunit = value.split(b' ')
        values = vaunit[0].split(b',')
        self.unit = vaunit[1]
        res = {}
        for val in values:
            key_val = val.split(b'=')
            res[key_val[0].decode()] = key_val[1].decode()
        return res
