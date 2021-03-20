Demo:

>>> from Crypto.Cipher import AES
>>> import Crypto.Cipher.AES
>>> from binascii import hexlify, unhexlify
>>> key = unhexlify('2b7e151628aed2a6abf7158809cf4f3c')
>>> IV = unhexlify('000102030405060708090a0b0c0d0e0f')
>>> plaintext1 = unhexlify('6bc1bee22e409f96e93d7e117393172a')
>>> plaintext2 = unhexlify('ae2d8a571e03ac9c9eb76fac45af8e51')
>>> plaintext3 = unhexlify('30c81c46a35ce411e5fbc1191a0a52ef')
>>> cipher = AES.new(key,AES.MODE_CBC,IV)
>>> ciphertext = cipher.encrypt(plaintext1 + plaintext2 + plaintext3)
>>> hexlify(ciphertext)
b'7649abac8119b246cee98e9b12e9197d5086cb9b507219ee95db113a917678b273bed6b8e3c1743b7116e69e22229516'
>>> decipher = AES.new(key,AES.MODE_CBC,IV)
>>> plaintext = decipher.decrypt(ciphertext)
>>> plaintext == plaintext1 + plaintext2 + plaintext3  # test if decryption was successful
True
>>> hexlify(plaintext)
b'6bc1bee22e409f96e93d7e117393172aae2d8a571e03ac9c9eb76fac45af8e5130c81c46a35ce411e5fbc1191a0a52ef'


    def encrypt(self, msg):
        msg = msg.encode()  # byte encode
        enc_msg = self.f.encrypt(msg)
        return enc_msg

    def decrypt(self, msg):
        dec_msg = self.f.decrypt(msg)
        return dec_msg


https://pycryptodome.readthedocs.io/en/latest/src/cipher/aes.html

