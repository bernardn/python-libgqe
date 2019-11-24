"""
Spectrum Analyser actions

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
from libgqe.protocol.GQRFC1701.v1_00 import SETSPECTRUMBAND, GETBANDDATA


class Spectrum(GQEMF):
    """Spectrum analyzer class"""
#    def __init__(self, *args, **kwargs):
#        pass

    def cmd_spectrum_set_band(self, band=None, *args, **kwargs):
        """Define spectrum analyzer band ID"""
        cmd = SETSPECTRUMBAND.SETSPECTRUMBAND(self.rw_functions, *args, **kwargs)
        cmd.send(band)

    def cmd_spectrum_get_band_data(self, *args, **kwargs):
        """Retrieve current spectrum analyzer band gain values"""
        cmd = GETBANDDATA.GETBANDDATA(self.rw_functions, *args, **kwargs)
        cmd.send()
        return cmd.response
