"""
GQ-RFC1701 protocol implementation: Command - GETSCREEN

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

from libgqe.protocol.GQRFC1701.v1_00 import Protocol


class GETSCREEN(Protocol):
    """ Gets the display screen in bitmap """
    ARGUMENTS = None
    WIDTH = 128
    HEIGHT = 64
    RESPONSE_TYPE = Protocol.Response.Bytes(int(WIDTH * HEIGHT / 8) + 1)

    def __init__(self, rw_connector=(None, None), *args, **kwargs):
        GQRFC1701.__init__(self, rw_connector, *args, **kwargs)
        self.response = b''

    def _parse_response(self, value):
        ddram = value
        # Transforms lcd paged RAM content to picture bit map with pixel(0,0) on top left
        r = bytearray(b'\x00' * self.WIDTH * self.HEIGHT)                      # Init buffer
        npcols = int(self.WIDTH / 8)                                           # number of byte columns in picture
        npages = int(self.HEIGHT / 8)                                          # number of pages of LCD RAM
        pdram = -1                                                             # LCD RAM byte pointer
        for page in range(0, npages):
            pprow = 8 * (npages - page - 1)                                    # picture row pointer for current page
            for column in range(0, self.WIDTH):
                dbit = 7 - column % 8                                          # destination bit position. lsb = 0
                pcol = int(column / 8)                                         # current picture byte column
                pdram += 1                                                     # next lcd ram byte
                for sbit in range(0, 8):
                    pbm = pcol + (pprow + 7 - sbit) * npcols                   # picture byte pointer
                    r[pbm] |= (2 ** sbit & ddram[pdram]) >> sbit << dbit       # set pixel
        return r
