"""
GQ-RFC1701 protocol v1.00 implementation

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

from libgqe.protocol.GQRFC1701 import Protocol

from libgqe.protocol.GQRFC1701 import POWER, CFGUPDATE, ECFG, FACTORYRESET, GETDATETIME, GETGYRO, GETSERIAL, GETCFG
from libgqe.protocol.GQRFC1701 import SETDATEDD, SETTIMESS, SETTIMEMM, SETTIMEHH, SETDATEYY, SETDATEMM, SETDATETIME, KEY

__all__ = [
    # Parent Classes
    "Protocol",
    # Commands
    "GETVER", "KEY", "KEYHOLD", "GETEMF", "GETEF", "GETBANDDATA", "GETMODE", "GETSCREEN",
    "GETCFG", "ECFG", "WCFG", "GETSERIAL", "POWER", "CFGUPDATE",
    "SETDATEYY", "SETDATEMM", "SETDATEDD", "SETTIMEHH", "SETTIMEMM", "SETTIMESS", "SETDATETIME", "GETDATETIME",
    "FACTORYRESET", "REBOOT",
    "GETGYRO", "SPEAKER", "GETVOLT", "ECHO",
    "SPIR", "SPIE", "GETRF", "SETSPECTRUMBAND", "RESETRFPEAK",
]
