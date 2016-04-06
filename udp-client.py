#!/usr/bin/python
'''UDP client for server'''
import socket
import sys

# Encryption
from Crypto.Cipher import AES
import base64

# Symetric secret key (must be multiple of 16)
# Must match the server
secret = "aaaabbbbccccdddd"

def dx(edata):
    ''' Decyption function '''
    PADDING = '{'
    DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e)).decode("UTF-8").rstrip(PADDING)
    return DecodeAES(AES.new(secret.encode()), edata)

def ex(data):
    ''' Encyption function '''
    BLOCK_SIZE = 16
    PADDING = '{'
    pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING
    EncodeAES = lambda c, s: base64.b64encode(c.encrypt(pad(s)))
    return EncodeAES(AES.new(secret.encode()), data)

# Command line args and usage statement
if (len(sys.argv) != 3):
    print("UDP client usage: ", sys.argv[0], " ip port")
    print("Example: ", sys.argv[0], "1.2.3.4 9999")
    sys.exit()

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip   = sys.argv[1]
port = int(sys.argv[2])

# Loop until quit
while True:

    # Collect user input
    cmd = input("cmd> ")

    if cmd == "":
        break

    # Encypt and send
    mystring = ex(cmd)
    sock.sendto(mystring, (ip, port))

    # Receive and decrypt
    data, addr = sock.recvfrom(4096)
    myreturn = dx(data)

    print(myreturn)

