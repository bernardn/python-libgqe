"""
GMC 2nd generation abstraction layer

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

from libgqe.unit import Unit

__all__ = [
    "GMC"
]
X_UNITS = [
    "GMC500",
    "GMC600",
    "GMC500Plus",
    "GMC600Plus",
]
FIRMWARE_REVISIONS = [
    "Re_1_00",
]

X_PROTO_MAP = {
    "GMC500": 'GQRFC1801',
    "GMC600": 'GQRFC1801',
    "GMC500Plus": 'GQRFC1801',
    "GMC600Plus": 'GQRFC1801',
    "GMC280": 'GQRFC1201',
    "GMC300": 'GQRFC1201',
    "GMC300Plus": 'GQRFC1201',
    "GMC320": 'GQRFC1201',
    # "For the GMC-300 V3.xx and earlier version, the serial port communication is based on a fixed baud rate. \
    #  Baud: 57600"
    # "GMC-300 Plus V4.xx and later version firmware": "GQRFC1201",
    # "For the GMC-300 V3.xx and earlier version, the serial port communication is based on a fixed baud rate.",
    # "For GMC-320, the serial port communication baud rate is variable. It should be one of the followings:",

}
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


class GMC(Unit):
    """GMC 2nd gen base class"""
    MODULES = ["RTC", "SPI"]
    CFG_SIZE = 512
    SPI_SIZE = 1048576
    CFG_ITEMS = []
    for i in range(len(CFG_ITEMS), CFG_SIZE):
        CFG_ITEMS.append(str(i))

    def __init__(self, **kwargs):
        Unit.__init__(self, **kwargs)
