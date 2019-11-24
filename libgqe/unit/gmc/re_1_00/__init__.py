"""
Abstraction layer for GMC firmware Re 1.00 and above


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
]

from libgqe.unit.gmc import GMC
from libgqe.protocol.GQRFC1801.v1_00 import GETVER, GETCFG, GETCPM, GETCPS, GETMAXCPS, GETVOLT, ALARM, Echo, SPEAKER
from libgqe.protocol.GQRFC1801.v1_00 import GETSERIAL, POWER, REBOOT, FACTORYRESET, GETGYRO, KEY


class Re_1_00(GMC):
    """Base class for GMC firmware Re 1.00 and above"""
    def __init__(self, **kwargs):
        GMC.__init__(self, **kwargs)
        # print("Initializing protocol GQRFC1801.V1_00 for Re 1.00")

    def cmd_get_identity(self, *args, **kwargs):            # pylint: disable=unused-argument
        """Retrieve unit identity: model, firmware revision and serial number"""
        cmd_v = GETVER.GETVER(self.rw_functions)
        cmd_v.send()
        cmd_s = GETSERIAL.GETSERIAL(self.rw_functions)
        cmd_s.send()
        return cmd_v.response[0], cmd_v.response[1], cmd_s.response

    def cmd_get_serial(self, *args, **kwargs):              # pylint: disable=unused-argument
        """Retrieve unit serial number"""
        cmd = GETSERIAL.GETSERIAL(self.rw_functions)
        cmd.send()
        return cmd.response

    def cmd_power(self, off_on=None, *args, **kwargs):      # pylint: disable=unused-argument
        """Turn the unit on/off"""
        cmd = POWER.POWER(self.rw_functions)
        cmd.send(off_on)

    def cmd_reboot(self, *args, **kwargs):                  # pylint: disable=unused-argument
        """Reboot the unit"""
        cmd = REBOOT.REBOOT(self.rw_functions)
        cmd.send()

    def cmd_reset_factory(self, *args, **kwargs):           # pylint: disable=unused-argument
        """Reset the unit to factory defaults"""
        cmd = FACTORYRESET.FACTORYRESET(self.rw_functions)
        cmd.send()

    def cmd_get_cfg(self, *args, raw=False, **kwargs):      # pylint: disable=unused-argument
        """Retrieve unit's configuration"""
        cmd = GETCFG.GETCFG(self.rw_functions)
        cmd.send()
        return cmd.response

    def cmd_get_cpm(self, *args, **kwargs):                 # pylint: disable=unused-argument
        """Retrieve counts per minute"""
        cmd = GETCPM.GETCPM(self.rw_functions)
        cmd.send()
        return cmd.response

    def cmd_get_cps(self, *args, **kwargs):                 # pylint: disable=unused-argument
        """Retrieve counts per second"""
        cmd = GETCPS.GETCPS(self.rw_functions)
        cmd.send()
        return cmd.response

    def cmd_get_cps_max(self, *args, **kwargs):             # pylint: disable=unused-argument
        """Retrieve counts per second peak"""
        cmd = GETMAXCPS.GETMAXCPS(self.rw_functions)
        cmd.send()
        return cmd.response

    def cmd_get_battery_voltage(self, *args, **kwargs):     # pylint: disable=unused-argument
        """Retrieve unit battery voltage value"""
        cmd = GETVOLT.GETVOLT(self.rw_functions)
        cmd.send()
        return cmd.response

    def cmd_get_gyroscope(self, *args, **kwargs):           # pylint: disable=unused-argument
        """Retrieve gyroscope values"""
        cmd = GETGYRO.GETGYRO(self.rw_functions)
        cmd.send()
        return cmd.response

    def cmd_key_press(self, key_id=None, *args, **kwargs):  # pylint: disable=unused-argument
        """Simulate a key press"""
        cmd = KEY.KEY(self.rw_functions)
        cmd.send(key_id)

    def cmd_alarm(self, on_off=None, *args, **kwargs):      # pylint: disable=unused-argument
        """Enable / disable the alarm"""
        cmd = ALARM.ALARM(self.rw_functions)
        cmd.send(on_off)

    def cmd_echo(self, off_on=None, *args, **kwargs):       # pylint: disable=unused-argument
        """Set unit echo ON or OFF"""
        cmd = Echo.Echo(self.rw_functions)
        cmd.send(off_on)

    def cmd_speaker(self, off_on=None, *args, **kwargs):    # pylint: disable=unused-argument
        """Set the speaker on/off"""
        cmd = SPEAKER.SPEAKER(self.rw_functions)
        cmd.send(off_on)
