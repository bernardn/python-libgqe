"""
Abstraction layer for firmware Re 1.00 and above

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

__all__ = [
    "Re_1_00",
    "rtc",
    "spectrum",
    "spi"
]

from libgqe.unit.gqemf import GQEMF
from libgqe.protocol.GQRFC1701.v1_00 import GETVER, GETEMF, GETEF, GETRF, RESETRFPEAK, GETMODE, GETVOLT, KEYHOLD, ECHO
from libgqe.protocol.GQRFC1701.v1_00 import GETSERIAL, GETGYRO, SPEAKER, REBOOT, GETSCREEN, GETCFG, POWER, FACTORYRESET
from libgqe.protocol.GQRFC1701.v1_00 import KEY


class Re_1_00(GQEMF):
    """Abstraction class for GQEMF firmware Re 1.00 and above"""
    def __init__(self, *args, **kwargs):
        GQEMF.__init__(self, *args, **kwargs)
        # print("Initializing protocol GQRFC1701.V1_00 for Re 1.00")

    def cmd_get_identity(self, *args, **kwargs):
        """Retrieve unit identity: model, firmware revision and serial number"""
        cmd_v = GETVER.GETVER(self.rw_functions, *args, **kwargs)
        cmd_v.send()
        cmd_s = GETSERIAL.GETSERIAL(self.rw_functions, *args, **kwargs)
        cmd_s.send()
        return cmd_v.response[0], cmd_v.response[1], cmd_s.response

    def cmd_get_serial(self, *args, **kwargs):
        """Retrieve unit serial number"""
        cmd = GETSERIAL.GETSERIAL(self.rw_functions, *args, **kwargs)
        cmd.send()
        return cmd.response

    def cmd_get_emf(self, *args, **kwargs):
        """Retrieve current EMF reading"""
        cmd = GETEMF.GETEMF(self.rw_functions, *args, **kwargs)
        cmd.send()
        return cmd.response

    def cmd_get_ef(self, *args, **kwargs):
        """Retrieve current EF reading"""
        cmd = GETEF.GETEF(self.rw_functions, *args, **kwargs)
        cmd.send()
        return cmd.response

    def cmd_get_rf(self, measurement='8GTOTALDENSITY', *args, **kwargs):
        """Retrieve current RF reading"""
        cmd = GETRF.GETRF(self.rw_functions, *args, **kwargs)
        cmd.send(measurement.upper())
        return cmd.response

    def cmd_reset_rf_peak(self, *args, **kwargs):
        """Retrieve current RF reading"""
        cmd = RESETRFPEAK.RESETRFPEAK(self.rw_functions, *args, **kwargs)
        cmd.send()

    def cmd_get_mode(self, *args, **kwargs):
        """Retrieve current unit operating mode"""
        cmd = GETMODE.GETMODE(self.rw_functions, *args, **kwargs)
        cmd.send()
        return cmd.response

    def cmd_get_battery_voltage(self, *args, **kwargs):
        """Retrieve unit battery voltage value"""
        cmd = GETVOLT.GETVOLT(self.rw_functions, *args, **kwargs)
        cmd.send()
        return cmd.response

    def cmd_get_gyroscope(self, *args, **kwargs):
        """Retrieve gyroscope values"""
        cmd = GETGYRO.GETGYRO(self.rw_functions, *args, **kwargs)
        cmd.send()
        return cmd.response

    def cmd_key_press(self, key_id=None, *args, **kwargs):
        """Simulate a key press"""
        cmd = KEY.KEY(self.rw_functions, *args, **kwargs)
        cmd.send(key_id)

    def cmd_key_hold(self, key_id=None, *args, **kwargs):
        """Simulate a key hold"""
        cmd = KEYHOLD.KEYHOLD(self.rw_functions, *args, **kwargs)
        cmd.send(key_id)

    def cmd_echo(self, off_on=None, *args, **kwargs):
        """Set unit echo ON or OFF"""
        cmd = ECHO.ECHO(self.rw_functions, *args, **kwargs)
        cmd.send(off_on)

    def cmd_speaker(self, off_on=None, *args, **kwargs):
        """Set the speaker on/off"""
        cmd = SPEAKER.SPEAKER(self.rw_functions, *args, **kwargs)
        cmd.send(off_on)

    def cmd_power(self, off_on=None, *args, **kwargs):
        """Turn the unit on/off"""
        cmd = POWER.POWER(self.rw_functions, *args, **kwargs)
        cmd.send(off_on)

    def cmd_reboot(self, *args, **kwargs):
        """Reboot the unit"""
        cmd = REBOOT.REBOOT(self.rw_functions, *args, **kwargs)
        cmd.send()

    def cmd_reset_factory(self, *args, **kwargs):
        """Reset the unit to factory defaults"""
        cmd = FACTORYRESET.FACTORYRESET(self.rw_functions, *args, **kwargs)
        cmd.send()

    def cmd_get_screen(self, *args, **kwargs):
        """Retrieve unit's display data. Available formats: bmp, pbm and raw."""
        cmd = GETSCREEN.GETSCREEN(self.rw_functions, *args, **kwargs)
        cmd.send()
        return cmd.response

    def cmd_get_cfg(self, *args, **kwargs):
        """Retrieve unit's configuration"""
        cmd = GETCFG.GETCFG(self.rw_functions, *args, cfg_size=self.CFG_SIZE, cfg_items=self.CFG_ITEMS, **kwargs)
        cmd.send()
        return cmd.response
