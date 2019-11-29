"""
GQ-RFC1701 protocol implementation: Command - WCFG

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


class WCFG(Protocol):
    """
    Write configuration data byte

    Note: due to the EEPROM technology used in hardware, bits can only be changed from 1 to 0
    without erasing the whole chip.

    Return: 0xAA, returns 0x55 if failed

    Firmware supported:  EMF360, EMF360+, EMF380, EMF360v2***, EMF360+v2***, EMF380v2***, EMF390***
    """
    ARGUMENTS = [
        Protocol.Argument.Numeric(0, 0),    # Address MSB
        Protocol.Argument.Numeric(0, 255),  # Address MLB
        Protocol.Argument.Numeric(0, 255)   # Data byte
    ]
    RESPONSE_TYPE = Protocol.Response.Byte('\xaa')
