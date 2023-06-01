"""
GQ-RFC1701 protocol implementation: Command - SPIR

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

import time
import struct
import datetime

from libgqe.protocol.SPIR import SPIR as SPIR_PROTO


class SPIR(SPIR_PROTO):
    """ Read SPI memory data (data log) """
    SRC = [
        "---"
        "Smart Meter",
        "Cell Tower",
        "Microwave",
        "WiFi/Phone",
        "Static",
        "AC EF",
        "Power Line"
    ]

    def decode_spi_chunk(self, data):
        pdb = 0  # Data byte pointer
        lnd = len(data)
        ts = 0
        dt = datetime.datetime.now()
        while pdb < lnd:
            if data[pdb:pdb+2] == b'\x55\xaa':    # Timestamp
                if lnd - pdb >= 8:
                    tim = datetime.datetime(
                        ord(data[pdb+2:pdb+3]) + 100 * int(dt.year / 100),
                        ord(data[pdb+3:pdb+4]),   # month
                        ord(data[pdb+4:pdb+5]),   # day
                        ord(data[pdb+5:pdb+6]),   # hour
                        ord(data[pdb+6:pdb+7]),   # minute
                        ord(data[pdb+7:pdb+8])    # second
                    )
                    pdb += 8
                    ts = time.mktime(tim.timetuple())
                else:
                    break
            elif data[pdb:pdb+2] == b'\xaa\x55':  # Data
                if lnd - pdb >= self.SPI_DATA_LENGTH:
                    emf = (data[pdb+2] * 16 + data[pdb+3] >> 4) + (data[pdb+3] & 15) / 10
                    ef = struct.unpack('<f', data[pdb+4:pdb+8])[0]
                    rf = struct.unpack('<f', data[pdb+8:pdb+12])[0]
                    src = "---"
                    if lnd - pdb >= 14 and data[pdb+12:pdb+13] == b'\x5a':  # Source
                        try:
                            src = self.SRC[ord(data[pdb+13:pdb+14])]
                        except IndexError:
                            src = "Mixed"
                        pdb += 2
                    yield {
                        'ts': datetime.datetime.fromtimestamp(ts),
                        'emf': emf, 'emf-unit': 'mG',
                        'ef': ef, 'ef-unit': 'V/m',
                        'rf': rf, 'rf-unit': 'pW/cm2',
                        'src': src
                    }
                    pdb += 12
                    ts += 1
                else:
                    break
            elif data[pdb:pdb+1] == b'\xff':    # Empty data
                self._chunk_remainder = b''
                raise SPIR.EmptyDataError()
            else:
                raise ValueError('Invalid SPI data chunk at address 0x{:x} : {}'.format(pdb, data[pdb:pdb+2]))

        self._chunk_remainder = data[pdb:]
