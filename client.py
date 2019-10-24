#!/usr/bin/python3

import socket
import sys
import time

# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = ("localhost", 8080)

for pings in range(10):
    start = time.time()
    client_socket.sendto(b"Hello, World!", dest)
    try:
        data, server = client_socket.recvfrom(1024)
        end = time.time()
        elapsed = end - start
        print(f'{data} {pings} {elapsed}')
    except socket.timeout:
        print('REQUEST TIMED OUT')
