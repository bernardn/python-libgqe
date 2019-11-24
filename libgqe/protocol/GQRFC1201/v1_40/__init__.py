"""
GQ-RFC1201 protocol v1.40 implementation

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

from libgqe.protocol.GQRFC1201 import GQRFC1201
from libgqe.protocol.GQRFC1201 import POWER, REBOOT
from libgqe.protocol.GQRFC1201 import CFGUPDATE, ECFG, FACTORYRESET, GETDATETIME, GETGYRO, GETSERIAL, GETVER, KEY, SPIR
from libgqe.protocol.GQRFC1201 import SETDATEDD, SETTIMESS, SETTIMEMM, SETTIMEHH, SETDATEYY, SETDATEMM, SETDATETIME


__all__ = [
    # Parent Classes
    "GQRFC1201", "V1_40",
    # Commands
    "CFGUPDATE", "ECFG", "FACTORYRESET", "GETDATETIME", "GETGYRO", "GETSERIAL", "GETVER", "KEY", "POWER", "REBOOT",
    "SETDATEDD", "SETTIMESS", "SETTIMEMM", "SETTIMEHH", "SETDATEYY", "SETDATEMM", "SETDATETIME", "SPIR",
]


class V1_40(GQRFC1201):
    """
    GQ-RFC1201 V1.40
    """
    def __init__(self, *args, **kwargs):
        GQRFC1201.__init__(self, *args, **kwargs)
        # print("Initializing protocol {}".format('GQRFC1201'))
