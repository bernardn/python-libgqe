"""
GQ-RFC protocols implementation: Command - SPIR

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

import sys

from libgqe.protocol import Protocol


class SPIR(Protocol):
    """ Read SPI data """
    ARGUMENTS = [Protocol.Argument.Numeric(0, 255)] * 5
    RESPONSE_TYPE = Protocol.Response.Bytes(4096)
    SPI_SIZE = 4096
    SPI_DATA_LENGTH = 12

    def __init__(self, rw_connectors, *args, **kwargs):
        Protocol.__init__(self, rw_connectors, *args, **kwargs)
        self._chunk_remainder = b''

    def get_all(self):
        """ Retrieve all SPI records from the unit """
        nbr = self.RESPONSE_TYPE.read_bytes
        nbh = int(nbr / 256)
        nbl = nbr % 256
        npg = int(self.SPI_SIZE / nbr)
        self._chunk_remainder = b''
        try:
            for i in range(0, npg):
                phi = int(i * nbr / 65536)
                pmi = int(((i * nbr) % 65536) / 256)
                plo = int((i * nbr) % 256)
                sys.stderr.write("\rReading address 0x{:02X}{:02X}{:02X}".format(phi, pmi, plo))
                self.send(phi, pmi, plo, nbh, nbl)
                if self.format == 'raw':
                    yield self.response
                else:
                    for record in self.decode_spi_chunk(self._chunk_remainder + self.response):
                        yield record
        except SPIR.EmptyDataError:
            pass
        except Exception as err:  # pylint: disable=broad-except
            sys.stderr.write("\nException in SPIR : {}".format(err))
        finally:
            sys.stderr.write("\n")

    @staticmethod
    def decode_spi_chunk(data):
        """ Default """
        return data

    class EmptyDataError(BaseException):
        """ Risen when no data has been received """
