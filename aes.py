from Crypto.Cipher import AES
from Crypto import Random
from binascii import hexlify, unhexlify
import hashlib
import base64

# PKCS5 padding
BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS) 
unpad = lambda s : s[0:-ord(s[-1])]

def encrypt(plaintext):
    passpharse = b'abcdefghijuklmno0123456789012345'
    salt = bytes([0, 0, 0, 0, 0, 0, 0, 0])
    # salt = Random.new().read(8)

    salted = bytes([])
    dx = bytes([])
    while (len(salted) < 48):
        dx = hashlib.md5(dx + passpharse + salt).digest()
        salted = salted + dx

    key = salted[:32]
    iv = salted[32:]
    iv = iv[:16]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(plaintext))
    encoded = base64.b64encode(b'Salted__' + salt + ciphertext)
    return str(encoded.decode('utf-8'))