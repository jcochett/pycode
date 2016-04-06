#!/usr/bin/python
'''A_simple_TCP_client'''

import socket

server_endpoint = ('localhost', 9999)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(server_endpoint)

print('The_connection_with ', sock.getpeername(), ' has_been_established')

message = "hola"
encoded_message = message.encode()
sock.send(encoded_message)

sock.close()
