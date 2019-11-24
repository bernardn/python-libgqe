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

from libgqe.unit.gqemf.re_1_00.spectrum import Spectrum as Spectrum_1_00
from libgqe.protocol.GQRFC1701.v2_00 import GETSPECTRUMFULLSCANFLAG, RESETBANDDATA


class Spectrum(Spectrum_1_00):
    """Spectrum analyzer class"""
    def cmd_spectrum_scan_complete(self, *args, **kwargs):
        """Flagged True when the whole spectrum band has been analyzed """
        cmd = GETSPECTRUMFULLSCANFLAG.GETSPECTRUMFULLSCANFLAG(self.rw_functions, *args, **kwargs)
        cmd.send()
        return cmd.response

    def cmd_spectrum_reset(self, *args, **kwargs):
        """Reset spectrum band data"""
        cmd = RESETBANDDATA.RESETBANDDATA(self.rw_functions, *args, **kwargs)
        cmd.send()
