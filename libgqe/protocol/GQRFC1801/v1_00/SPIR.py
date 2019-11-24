"""
GQ-RFC1801 protocol implementation: Command - SPIR

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

from libgqe.protocol.SPIR import SPIR as SPIR_PROTO


class SPIR(SPIR_PROTO):
    """ Read unit's SPI data (data log) """
    def decode_spi_chunk(self, data):
        # Todo Get SPI log format. Undefined in available protocol paper.
        return data

    class EmptyDataError(BaseException):
        """Risen when no data has been received"""
