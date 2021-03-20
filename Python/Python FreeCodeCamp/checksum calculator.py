from crccheck.crc import CrcX25

data = bytearray([0x04,0x00,0x02,0x00,0xff,0xff])
x25_crc = str(hex(CrcX25.calc(data)))[2:].upper()
if len(x25_crc) < 4:
    x25_crc = (4 - len(x25_crc)) * '0' + x25_crc
x25_crc = x25_crc[2:4] + x25_crc[0:2]
print(x25_crc)
