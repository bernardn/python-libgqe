"""
SPI actions

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

from libgqe.unit.gqemf import GQEMF
from libgqe.protocol.GQRFC1701.v1_00 import SPIR, SPIE


class SPI(GQEMF):
    """SPI class"""
    SPI_SIZE = 0

#    def __init__(self, *args, **kwargs):
#       super().__init__(*args, **kwargs)

    def cmd_spi_get(self, *args, **kwargs):
        """Retrieve unit's data log"""
        cmd = SPIR.SPIR(self.rw_functions, *args, **kwargs)
        cmd.SPI_SIZE = self.SPI_SIZE
        for rec in cmd.get_all():
            yield rec

    def cmd_spi_erase(self, *args, **kwargs):
        """Erase unit's data log"""
        cmd = SPIE.SPIE(self.rw_functions, *args, **kwargs)
        cmd.send()
