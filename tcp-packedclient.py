#!/usr/bin/python
'''A_packed_TCP_client'''

import socket
import struct

max_message_size = 100

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 9998))

unsigned_int8 = 3
signed_int16 = -2442
string = "Hello"
float32 = 3.14

message = struct.pack('B', unsigned_int8)
message += struct.pack('>h', signed_int16)
message += string.encode()
message += struct.pack('>f', float32)

sock.sendall(message)

sock.close()

