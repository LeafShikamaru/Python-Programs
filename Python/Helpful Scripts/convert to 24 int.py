value2=bytearray([0x60,0x54,0x00])
result = str(-65536 * (value2[0]) + (256 * (value2[1]) + (value2[2])))
print(result)
