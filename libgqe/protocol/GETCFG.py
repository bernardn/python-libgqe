"""
GQ-RFCXXXX protocols implementation: Command - GETCFG

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


class GETCFG(Protocol):
    """ Get configuration data """
    CFG_ITEMS = []
    CFG_SIZE = 256
    ARGUMENTS = None
    RESPONSE_TYPE = Protocol.Response.Bytes(CFG_SIZE)
    for i in range(len(CFG_ITEMS), CFG_SIZE):
        CFG_ITEMS.append(str(i))

    def __init__(self, *args, cfg_size=CFG_SIZE, cfg_items=tuple(CFG_ITEMS), **kwargs):
        """
            :arg: cfg_size
            :arg: cfg_items
        """
        super().__init__(*args, **kwargs)
        self.RESPONSE_TYPE.read_bytes = cfg_size
        self.cfg_items = cfg_items

    def _parse_response(self, value):
        res = {}
        for ptr in range(0, len(self.cfg_items)):
            res[self.cfg_items[ptr]] = value[ptr]
        return res
