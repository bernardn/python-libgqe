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
        "LargeFontMode",                 # 0x0A
        "AlarmType",                     # 0x0B  1=beep,2=ghost,0=siren
        "EmfAlarm",
        "EfAlarm",
        "RfAlarm",
        "CumulativeTimeoutForRFGraph",   # 0x0F
        "LedOnOff",
        "BaseFrequency",
        "ChannelSpacing",
        "Bandwidth",
        "ZeroCalibrationByte0",          # 0x14
        "ZeroCalibrationByte1",
        "ZeroCalibrationByte2",
        "ZeroCalibrationByte3",
        "Reserved_01",
        "RfDensityUnit",                 # 0x19
        "RfBrowserScale",
        "LargeFontEMForRF",
        "SpiSaveData",                   # 0x1C
        "SpiCircularAddress",
        "SoundVolume",                   # 0x1E
        "EmfUnit",                       # 0x1F 0=mG; 1=uT
        "RfSensitivity"                  # 0x20 0=standard; 1=sensitive;
    ]

    def __init__(self, *args, **kwargs):
        Unit.__init__(self, *args, **kwargs)
