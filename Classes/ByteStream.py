import traceback
import zlib
from io import BufferedReader, BytesIO

from Classes.BitsUtils import BitsUtils


class ByteStream(BufferedReader):
    def __init__(self, messageBuffer):
        super().__init__(BytesIO(messageBuffer))
        self.bitoffset = 0
        self.bitsBuf = None

    # region Read

    def readByte(self):
        self.checkBitOffset()
        return self.read(1)

    def readBytes(self, length):
        self.checkBitOffset()
        return self.read(length)

    def readBytesWithoutLength(self):
        self.checkBitOffset()
        length = self.readInt()
        if length != -1:
            return self.read(length)
        else:
            return b''

    def readInt8(self, endian="big"):
        self.checkBitOffset()
        return int.from_bytes(self.read(1), endian, signed=True)

    def readInt16(self, endian="big"):
        self.checkBitOffset()
        return int.from_bytes(self.read(2), endian, signed=True)

    def readInt24(self, endian="big"):
        self.checkBitOffset()
        return int.from_bytes(self.read(3), endian, signed=True)

    def readInt(self, endian="big"):
        self.checkBitOffset()
        return int.from_bytes(self.read(4), endian, signed=True)

    def readUInt8(self, endian="big"):
        self.checkBitOffset()
        return int.from_bytes(self.read(1), endian, signed=False)

    def readUInt16(self, endian="big"):
        self.checkBitOffset()
        return int.from_bytes(self.read(2), endian, signed=False)

    def readUInt24(self, endian="big"):
        self.checkBitOffset()
        return int.from_bytes(self.read(3), endian, signed=False)

    def readUInt(self, endian="big"):
        self.checkBitOffset()
        return int.from_bytes(self.read(4), endian, signed=False)

    def readLong(self):
        result = []
        result.append(self.readInt())
        result.append(self.readInt())
        return result

    def readVLong(self):
        result = []
        result.append(self.readVint())
        result.append(self.readVint())
        return result

    def readDataReference(self):
        result = []
        result.append(self.readVint())
        if result[0] == 0:
            result[0] = -1
            result.append(0)
            return result
        result.append(self.readVint())
        return result

    def readString(self):
        lenght = self.readInt()
        if lenght == -1 or lenght == 0:
            return b""
        else:
            try:
                decoded = self.read(lenght)
                return decoded.decode('utf-8')
            except Exception:
                print(traceback.format_exc())

    def readCompressedString(self):
        data_length = self.readInt()
        self.readInt(endian='little')
        return zlib.decompress(self.readBytes(data_length - 4))

    def readVint(self):
        self.checkBitOffset()
        result = 0
        shift = 0
        while True:
            byte = self.readUInt8()
            if True and shift == 0:
                seventh = (byte & 0x40) >> 6  # save 7th bit
                msb = (byte & 0x80) >> 7  # save msb
                n = byte << 1  # rotate to the left
                n = n & ~0x181  # clear 8th and 1st bit and 9th if any
                byte = n | (msb << 7) | seventh  # insert msb and 6th back in
            result |= (byte & 0x7f) << shift
            shift += 7
            if not (byte & 0x80):
                break
        return (result >> 1) | (-(result & 1))

    def readBoolean(self):
        bitstreamS = BitsUtils.reverseBits(BytesIO(self.peek()).read(1))
        result = bitstreamS.read(bool, self.bitoffset + 1)[self.bitoffset]
        self.bitoffset += 1
        return result

    # endregion

    # region Write

    def writeBytes(self, data):
        self.messagePayload += data

    def writeInt8(self, data, endian="big"):
        self.checkBitOffset()
        if type(data) == str:
            data = int(data)
        self.messagePayload += data.to_bytes(1, endian, signed=True)

    def writeInt16(self, data, endian="big"):
        self.checkBitOffset()
        if type(data) == str:
            data = int(data)
        self.messagePayload += data.to_bytes(2, endian, signed=True)

    def writeInt24(self, data, endian="big"):
        self.checkBitOffset()
        if type(data) == str:
            data = int(data)
        self.messagePayload += data.to_bytes(3, endian, signed=True)

    def writeInt(self, data, endian="big"):
        self.checkBitOffset()
        if type(data) == str:
            data = int(data)
        self.messagePayload += data.to_bytes(4, endian, signed=True)

    def writeUInt8(self, data, endian="big"):
        self.checkBitOffset()
        if type(data) == str:
            data = int(data)
        self.messagePayload += data.to_bytes(1, endian, signed=False)

    def writeUInt16(self, data, endian="big"):
        self.checkBitOffset()
        if type(data) == str:
            data = int(data)
        self.messagePayload += data.to_bytes(2, endian, signed=False)

    def writeUInt24(self, data, endian="big"):
        self.checkBitOffset()
        if type(data) == str:
            data = int(data)
        self.messagePayload += data.to_bytes(3, endian, signed=False)

    def writeUInt(self, data, endian="big"):
        self.checkBitOffset()
        if type(data) == str:
            data = int(data)
        self.messagePayload += data.to_bytes(4, endian, signed=False)

    def writeHexa(self, data):
        if data:
            if data.startswith('0x'):
                data = data[2:]
            self.messagePayload += bytes.fromhex(''.join(data.split()).replace('-', ''))

    def writeLong(self, high, low):
        self.writeInt(high)
        self.writeInt(low)

    def writeVLong(self, high, low):
        self.writeVint(high)
        self.writeVint(low)

    def writeDataReference(self, high=-1, low=0):
        if high == -1 or high == 0:
            self.writeVint(0)
            return
        self.writeVint(high)
        self.writeVint(low)

    def writeString(self, text=None):
        if text == None:
            self.writeInt(-1)
        else:
            if type(text) == bytes:
                encoded = text
            else:
                encoded = text.encode('utf-8')
            self.writeInt(len(encoded))
            self.messagePayload += encoded

    def writeVint(self, data):
        self.checkBitOffset()
        if type(data) == str:
            data = int(data)
        final = b''
        if (data & 2147483648) != 0:
            if data >= -63:
                final += (data & 0x3F | 0x40).to_bytes(1, 'big', signed=False)
            elif data >= -8191:
                final += (data & 0x3F | 0xC0).to_bytes(1, 'big', signed=False)
                final += ((data >> 6) & 0x7F).to_bytes(1, 'big', signed=False)
            elif data >= -1048575:
                final += (data & 0x3F | 0xC0).to_bytes(1, 'big', signed=False)
                final += ((data >> 6) & 0x7F | 0x80).to_bytes(1, 'big', signed=False)
                final += ((data >> 13) & 0x7F).to_bytes(1, 'big', signed=False)
            elif data >= -134217727:
                final += (data & 0x3F | 0xC0).to_bytes(1, 'big', signed=False)
                final += ((data >> 6) & 0x7F | 0x80).to_bytes(1, 'big', signed=False)
                final += ((data >> 13) & 0x7F | 0x80).to_bytes(1, 'big', signed=False)
                final += ((data >> 20) & 0x7F).to_bytes(1, 'big', signed=False)
            else:
                final += (data & 0x3F | 0xC0).to_bytes(1, 'big', signed=False)
                final += ((data >> 6) & 0x7F | 0x80).to_bytes(1, 'big', signed=False)
                final += ((data >> 13) & 0x7F | 0x80).to_bytes(1, 'big', signed=False)
                final += ((data >> 20) & 0x7F | 0x80).to_bytes(1, 'big', signed=False)
                final += ((data >> 27) & 0xF).to_bytes(1, 'big', signed=False)
        else:
            if data <= 63:
                final += (data & 0x3F).to_bytes(1, 'big', signed=False)
            elif data <= 8191:
                final += (data & 0x3F | 0x80).to_bytes(1, 'big', signed=False)
                final += ((data >> 6) & 0x7F).to_bytes(1, 'big', signed=False)
            elif data <= 1048575:
                final += (data & 0x3F | 0x80).to_bytes(1, 'big', signed=False)
                final += ((data >> 6) & 0x7F | 0x80).to_bytes(1, 'big', signed=False)
                final += ((data >> 13) & 0x7F).to_bytes(1, 'big', signed=False)
            elif data <= 134217727:
                final += (data & 0x3F | 0x80).to_bytes(1, 'big', signed=False)
                final += ((data >> 6) & 0x7F | 0x80).to_bytes(1, 'big', signed=False)
                final += ((data >> 13) & 0x7F | 0x80).to_bytes(1, 'big', signed=False)
                final += ((data >> 20) & 0x7F).to_bytes(1, 'big', signed=False)
            else:
                final += (data & 0x3F | 0x80).to_bytes(1, 'big', signed=False)
                final += ((data >> 6) & 0x7F | 0x80).to_bytes(1, 'big', signed=False)
                final += ((data >> 13) & 0x7F | 0x80).to_bytes(1, 'big', signed=False)
                final += ((data >> 20) & 0x7F | 0x80).to_bytes(1, 'big', signed=False)
                final += ((data >> 27) & 0xF).to_bytes(1, 'big', signed=False)
        self.messagePayload += final

    def writeBoolean(self, value, isByte=0):
        if isByte == 1:
            self.writeUInt8(value)
        else:
            if self.bitsBuf == None:
                self.bitsBuf = BitsUtils.getBitstream()
            self.bitsBuf.write(value)

    def writeCompressedString(self, data):
        compressedText = zlib.compress(data)
        self.writeInt(len(compressedText) + 4)
        self.writeInt(len(data), "little")
        self.messagePayload += compressedText

    # endregion

    # region Utility

    def checkBitOffset(self):
        if self.bitsBuf != None and len(self.bitsBuf) < 8:
            bitsLength = len(self.bitsBuf)
            bools = self.bitsBuf.read(bool, len(self.bitsBuf))
            while bitsLength < 8:
                bools.append(False)
                bitsLength += 1
            self.messagePayload += BitsUtils.reverseBits(bools).read(bytes)
            self.bitsBuf = None
        elif 1 <= self.bitoffset <= 8:
            self.read(1)
            self.bitoffset = 0

    # endregion