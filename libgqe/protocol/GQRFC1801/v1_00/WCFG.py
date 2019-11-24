"""
GQ-RFC1801 protocol implementation: Command - WCFG

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
from libgqe.protocol.GQRFC1801 import GQRFC1801


class WCFG(GQRFC1801):
    """
    Write configuration data byte

    Note: due to the EEPROM technology used in hardware, bits can only be changed from 1 to 0
    without erasing the whole chip.

    Return: 0xAA, returns 0x55 if failed
    """
    ARGUMENTS = [
        Protocol.Argument.Numeric(0, 1),    # Address MSB
        Protocol.Argument.Numeric(0, 255),  # Address MLB
        Protocol.Argument.Numeric(0, 255)   # Data byte
    ]
    RESPONSE_TYPE = Protocol.Response.Byte('\xaa')
