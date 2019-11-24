"""
GMC SPI Actions

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

from libgqe.unit.gmc import GMC
from libgqe.protocol.GQRFC1801.v1_00 import SPIR


class SPI(GMC):
    """Base class for GMC SPI"""
    SPI_SIZE = 0

    def cmd_spi_get(self, *args, **kwargs):
        """Retrieve unit's data log"""
        cmd = SPIR.SPIR(self.rw_functions, *args, **kwargs)
        cmd.SPI_SIZE = self.SPI_SIZE
        for val in cmd.get_all():
            yield val
