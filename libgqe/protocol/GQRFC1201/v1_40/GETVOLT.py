"""
GQ-RFC1201 protocol implementation: Command - GETVOLT

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
from libgqe.protocol.GQRFC1201 import GQRFC1201


class GETVOLT(GQRFC1201):
    """ Gets the battery voltage """
    ARGUMENTS = None
    RESPONSE_TYPE = Protocol.Response.Bytes(1)

    @staticmethod
    def _parse_response(value):
        return ord(value)
