"""
GQ-EMF360 unit layer

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


class GQEMF360(GQEMF):
    """GQEMF 360 unit abstraction class"""
    MODULES = []

    def __init__(self, *args, **kwargs):
        GQEMF.__init__(self, *args, **kwargs)
