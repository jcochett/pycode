#!/usr/bin/python
'''A packed TCP receiver'''

import socket
import struct

max_message_size = 100

listening_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listening_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listening_socket.bind(('', 9998))
listening_socket.listen(1)

#print ('I_am ', listening_socket.getsockname(), ' and_I_am_listening_...')

serving_socket = listening_socket.accept()
message = serving_socket[0].recv(max_message_size)

print(struct.unpack('>Bh5sf', message))
length = struct.unpack("B", message[0:1])[0]
print("length: ", length)
a,b,c,d = (struct.unpack('>Bh5sf', message))
print(a)
print(b)
print(c.decode())
print(d)
#print("unpacked string: ", unpacked_string.decode())

serving_socket[0].close()


