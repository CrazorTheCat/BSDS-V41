from bitstream import BitStream


class BitsUtils:
    def reverseBits(bits):
        boolStream = BitStream(bits)
        bools = boolStream.read(bool, 8)
        bools.reverse()
        return BitStream(bools)

    def getBitstream(byte=None):
        return BitStream(byte)