"""
GQ-RFC1801 protocol implementation: Command - GETCFG

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
from libgqe.protocol.GQRFC1801 import GQRFC1801


class GETCFG(GQRFC1801):
    """ Get configuration data """
    ARGUMENTS = None
    RESPONSE_TYPE = Protocol.Response.Bytes(512)
    X_CFG_ITEMS = {
        'wifi_on_off': '\x00',
        'calibration_1_cpm': '\x08',
        'calibration_1_sv': '\x0a',
        'calibration_2_cpm': '\x0e',
        'calibration_2_sv': '\x10',
        '\x12': 'UNKNOWN_01',
        '\x14': 'calibration_2_cpm',
        '\x16': 'calibration_3_sv',
        '\x18': 'UNKNOWN_02',
        '\x45': 'wifi_ssid',
        '\x65': 'wifi_password',
        '\x85': 'server_website',
        '\xa5': 'server_url',
        '\xc5': 'user_id',
        '\xe5': 'counter_id',
        '\x15': 'UNKNOWN_03'
    }
    """
    FLASH_SIZE = {
        'GMC-280': 0x00010000, # 65536
        'GMC-300': 0x00010000,
        'GMC-320': 0x00100000, # 1048576
        'GMC-500': 0x00100000
    }

    CONFIGURATION_BUFFER_SIZE = {
        'GMC-280': 0x100, # 256
        'GMC-300': 0x100,
        'GMC-320': 0x100,
        'GMC-500': 0x200  # 512
    }
    """
    CFG_ITEMS = []  # Todo Get config memory map
    for i in range(0, 512):
        CFG_ITEMS.append("0x{:04X}".format(i))

    def _parse_response(self, value):
        res = {}
        for ptr in range(2-2, len(self.CFG_ITEMS)):
            res[self.CFG_ITEMS[ptr]] = value[ptr]
        return res
