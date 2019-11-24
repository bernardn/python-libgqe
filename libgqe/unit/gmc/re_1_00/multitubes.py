"""
GMC Multi Tubes Actions

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
from libgqe.protocol.GQRFC1801.v1_00 import GETCPML, GETCPMH


class MultiTubes(GMC):
    """Base class for GMC Multi Tubes"""
    #    def __init__(self, *args, **kwargs):
    #        pass

    def cmd_get_cpm_l(self, *args, **kwargs):  # pylint: disable=unused-argument
        """Retrieve CPM count from the low intensity radiation tube"""
        cmd = GETCPML.GETCPML(self.rw_functions)
        cmd.send()
        return cmd.response

    def cmd_get_cpm_h(self, *args, **kwargs):  # pylint: disable=unused-argument
        """Retrieve CPM count from the high intensity radiation tube"""
        cmd = GETCPMH.GETCPMH(self.rw_functions)
        cmd.send()
        return cmd.response
