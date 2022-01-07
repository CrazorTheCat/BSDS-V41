import zlib
from io import BufferedReader, BytesIO

from Classes.Logic.LogicLong import LogicLong
from Classes.Debugger import Debugger


class ByteStreamHelper:
    def readDataReference(self):
        result = []
        result.append(self.readVInt())
        if not result[0]:
            return None
        result.append(self.readVInt())
        return result

    def writeDataReference(self, high, low):
        self.writeVInt(high)
        if high != 0:
            self.writeVInt(low)

    def compress(self, data):
        compressedText = zlib.compress(data)
        self.writeInt(len(compressedText) + 4)
        self.writeIntLittleEndian(len(data))
        self.buffer += compressedText

    def decompress(self):
        data_length = self.readInt()
        self.readIntLittleEndian()
        return zlib.decompress(self.readBytes(data_length - 4))

    def decodeIntList(self):
        length = self.readVInt()
        intList = []
        for i in range(length):
            intList.append(self.readVInt())

    def decodeLogicLong(self, logicLong):
        high = self.readVInt()
        logicLong.high = high
        low = self.readVInt()
        logicLong.low = low

    def decodeLogicLongList(self):
        length = self.readVInt()
        logicLongList = []
        for i in range(length):
            logicLongList.append(LogicLong(self.readVInt(), self.readVInt()))
        return logicLongList

    def encodeIntList(self, intList):
        length = len(intList)
        self.writeVInt(length)
        for i in intList:
            self.writeVInt(i)

    def encodeLogicLong(self, logicLong: LogicLong):
        self.writeVInt(logicLong.getHigherInt(self))
        self.writeVInt(logicLong.getLowerInt(self))

    def encodeLogicLongList(self, logicLongList):
        length = len(logicLongList)
        self.writeVInt(self, length)
        for logicLong in logicLongList:
            self.writeVInt(logicLong.getHigherInt(self))
            self.writeVInt(logicLong.getLowerInt(self))

    def readBattlePlayerMap(self, fields):
        if self.readBoolean() & 1 != 0:
            LogicBattlePlayerMap.decode(self, fields) # whatever i will finish it in a far futur :trolled:
        return fields