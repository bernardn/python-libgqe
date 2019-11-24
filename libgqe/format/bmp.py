"""
BMP Bitmap image formatter

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

from struct import pack
from libgqe.format import Format


class Bmp(Format):
    """BMP Bitmap image formatter class"""
    def __init__(self, *args, width=128, height=64, **kwargs):
        super().__init__(self, *args, **kwargs)
        self.width = width
        self.height = height

    def format(self, data):
        """format raw bitmap data to bmp format"""
        ppicdata = 62  # Picture data pointer
        filesize = ppicdata + len(data)

        img = b''
        # File Header
        img += b'BM'  # 0x00 Magic Number
        img += pack('<i', filesize)  # 0x02 FileSize bytes
        img += b'\x00\x00\x00\x00'  # 0x06 Null
        img += pack('<i', ppicdata)  # 0x0a Offset bytes. Offset to start of Pixel Data
        # Image Header
        img += b'\x28\x00\x00\x00'  # 0x0e BiSize. Header Size - Must be at least 40
        img += pack('<i', self.width)  # 0x12 BiWidth. Image Width
        img += pack('<i', -self.height)  # 0x16 BiHeight. Image Height
        img += b'\x01\x00'  # 0x1a BiPlanes. 1
        img += b'\x01\x00'  # 0x1c BiBitCount. Bits per pixel
        img += b'\x00\x00\x00\x00'  # 0x1e BiCompression. Compression mode
        img += b'\x00\x00\x00\x00'  # 0x22 BiSizeImage. 0 for uncompressed
        img += b'\x00\x00\x00\x00'  # 0x26 biXPelsPerMeter
        img += b'\x00\x00\x00\x00'  # 0x2a biYPelsPerMeter
        img += b'\x02\x00\x00\x00'  # 0x2e biClrUsed. Number Color Map entries that are actually used
        img += b'\x00\x00\x00\x00'  # 0x32 biClrImportant. Number of significant colors
        # Color Table
        img += b'\xff\xe0\xd0\x00'  # 0x36 Color 0
        img += b'\x28\x38\x28\x00'  # 0x3a Color 1
        # Picture Data
        self.write(img)
        self.write(data)            # 0x3e Picture data
