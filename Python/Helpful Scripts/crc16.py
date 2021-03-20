def crc16(data: bytes, poly=0x8408):
    '''
    CRC-16-CCITT Algorithm
    '''
    data = bytearray(data)
    crc = 0xFFFF
    for b in data:
        cur_byte = 0xFF & b
        for _ in range(0, 8):
            if (crc & 0x0001) ^ (cur_byte & 0x0001):
                crc = (crc >> 1) ^ poly
            else:
                crc >>= 1
            cur_byte >>= 1
    crc = (~crc & 0xFFFF)
    crc = (crc << 8) | ((crc >> 8) & 0xFF)
    
    return crc & 0xFFFF

# checksum calculation for CRC x-25
x25_crc = str(hex(CrcX25.calc(final)))[2:].upper()
if len(x25_crc) < 4:
    x25_crc = (4 - len(x25_crc)) * '0' + x25_crc
x25_crc = x25_crc[2:4] + x25_crc[0:2]
check = bytes.fromhex(x25_crc) # checksum to bytes
# checksum calculation for CRC x-25 end