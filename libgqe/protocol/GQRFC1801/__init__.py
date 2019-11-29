"""
GQ-RFC1801 protocol implementation

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

from libgqe.protocol import Protocol
from libgqe.protocol import POWER, REBOOT
from libgqe.protocol import GETCFG, CFGUPDATE, ECFG, FACTORYRESET, GETDATETIME, GETGYRO, GETSERIAL, KEY, GETVER
from libgqe.protocol import SETDATEDD, SETTIMESS, SETTIMEMM, SETTIMEHH, SETDATEYY, SETDATEMM, SETDATETIME, SPIR

__all__ = [
    # Parent Classes
    "Protocol",
    # Commands
    "CFGUPDATE", "ECFG", "FACTORYRESET", "GETDATETIME", "GETGYRO", "GETSERIAL", "GETVER", "KEY", "POWER", "REBOOT",
    "SETDATEDD", "SETTIMESS", "SETTIMEMM", "SETTIMEHH", "SETDATEYY", "SETDATEMM", "SETDATETIME", "SPIR", "GETCFG"
]
