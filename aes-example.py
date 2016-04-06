#!/usr/bin/python

from Crypto.Cipher import AES
import base64

secret = "aaaabbbbccccdddd"

def decryption(edata):
    PADDING = '{'
    DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e)).decode("UTF-8").rstrip(PADDING)
    return DecodeAES(AES.new(secret.encode()), edata)

def encryption(data):
    BLOCK_SIZE = 16
    PADDING = '{'
    pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING
    EncodeAES = lambda c, s: base64.b64encode(c.encrypt(pad(s)))
    return EncodeAES(AES.new(secret.encode()), data)

mystring = "hello"
print(mystring)
encr = encryption(mystring)
print(encr)
dencr = decryption(encr)
print(dencr)
