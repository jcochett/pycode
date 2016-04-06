#!/usr/bin/python
'''A simple TCP receiver'''

import socket

listening_adapter = '' # Listen to all adapters
listening_port = 9999
listening_queue_size = 0 
listening_endpoint = (listening_adapter, listening_port)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(listening_endpoint)

print ('I_am ', sock.getsockname(), ' and_I_am_listening_...')

sock.listen(listening_queue_size)
connection = sock.accept()
(sock,sender) = connection

print ('A_connection_with ', sender, ' has_been_established')

longest_message_size = 100
message = sock.recv(longest_message_size)
decoded_message = message.decode()

print ('"', decoded_message, '" ', 'is_received_from ', sender)

sock.close()
