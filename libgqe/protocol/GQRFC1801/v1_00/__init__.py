"""
GQ-RFC1801 v1.00 protocol implementation

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

from libgqe.protocol.GQRFC1801 import Protocol, GETCFG
from libgqe.protocol.GQRFC1801 import POWER, REBOOT, CFGUPDATE, ECFG, FACTORYRESET, GETDATETIME, GETGYRO, GETSERIAL, KEY
from libgqe.protocol.GQRFC1801 import SETDATEDD, SETTIMESS, SETTIMEMM, SETTIMEHH, SETDATEYY, SETDATEMM, SETDATETIME

__all__ = [
    # Parent Classes
    "Protocol",

    # Commands
    "ALARM", "GETVER",
    "GETCFG", "ECFG", "WCFG", "GETSERIAL", "POWER", "CFGUPDATE", "KEY",
    "SETDATEYY", "SETDATEMM", "SETDATEDD", "SETTIMEHH", "SETTIMEMM", "SETTIMESS", "GETDATETIME", "SETDATETIME",
    "FACTORYRESET", "REBOOT",
    "GETGYRO", "SPEAKER", "GETVOLT", "Echo",
    "SPIR",
    "GETCPM", "GETCPMH", "GETCPML", "GETCPS", "GETMAXCPS",

]
