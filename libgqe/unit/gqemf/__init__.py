"""
GQ-EMF units abstraction layer

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
    "GQEMF"
]
X_UNIT_MODELS = [
    "GQEMF360",
    "GQEMF360Plus",
    "GQEMF380",
    "GQEMF390",
]
FIRMWARE_REVISIONS = [
    "re_1_00",
    "re_2_00",
    "re_2_16",
]


class GQEMF(Unit):
    """GQEMF units base class"""
    BAUD_RATE = 115200
    CFG_SIZE = 256
    CFG_ITEMS = [
        "PowerOnOff",                    # address 0x00
        "SpeakerOnOff",
        "IdleDisplayMode",
        "BackLightTimeoutSeconds",
        "IdleTextState",
        "SwivelDisplay",                 # 0x05
        "nDisplayContrast",
        "nLargeFontMode",
        "nLCDBackLightLevel",
        "nReverseDisplayMode",
        "LARGEFONTMODE",                 # 0x0A
        "ALARMTYPE",
        "EMFALARM",
        "EFALARM",
        "RFALARM",
        "CUMMULATIVETIMEOUTFORRFGRAPH",  # 0x0F
        "LED_ONOFF",
        "Base_Frequency",
        "Channel_Spacing",
        "Bandwidth",
        "ZeroCalibrationByte0",          # 0x14
        "ZeroCalibrationByte1",
        "ZeroCalibrationByte2",
        "ZeroCalibrationByte3",
        "Reserved",
        "RfDensityUnit",                 # 0x19
        "RfBrowserScale",
        "LargeFontEMForRF",
        "SpiSaveData",                   # 0x1C
        "SpiCircularAddress",
        "MaximumBytes",                  # 0x1E
    ]

    def __init__(self, *args, **kwargs):
        Unit.__init__(self, *args, **kwargs)
