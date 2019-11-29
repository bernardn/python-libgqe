"""
GQ-RFC1201 protocol implementation

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
from libgqe.protocol import CFGUPDATE, GETCFG, ECFG, FACTORYRESET, GETDATETIME, GETGYRO, GETSERIAL, GETVER, KEY, SPIR
from libgqe.protocol import SETDATEDD, SETTIMESS, SETTIMEMM, SETTIMEHH, SETDATEYY, SETDATEMM, SETDATETIME


__all__ = [
    # Parent Classes
    "Protocol", "GQRFC1201",
    # Commands
    "CFGUPDATE", "ECFG", "FACTORYRESET", "GETDATETIME", "GETGYRO", "GETSERIAL", "GETVER", "KEY", "POWER", "REBOOT",
    "SETDATEDD", "SETTIMESS", "SETTIMEMM", "SETTIMEHH", "SETDATEYY", "SETDATEMM", "SETDATETIME", "SPIR", "GETCFG"
]


class GQRFC1201(Protocol):
    """
    Base class for Commands to be sent to the unit.
    UNITS = [
    GMC-500, GMC-500+, GMC-600, GMC-600+
    ]
    """

    def __init__(self, *args, **kwargs):
        Protocol.__init__(self, *args, **kwargs)
        # print("Initializing protocol {}".format('GQRFC1201'))
