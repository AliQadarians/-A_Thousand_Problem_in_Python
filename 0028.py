import struct
calcSize = struct.calcsize("P")
print("{} byte ".format(calcSize))
print("{} bit".format(calcSize*8))