import socket
import time
import struct
import numpy as np

# Create socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = ('10.0.0.1', 5005)
print ' [*] starting up on %s port %s' % server_address
sock.bind(server_address)

# Address to send message
_address = ('10.0.0.2', 5005)


for i in range(1000):
    # data to send
    data_notpacked = [i, 5, 1000-i]

    # packing data into uint32
    _data = struct.pack('%sI' % len(data_notpacked), *data_notpacked)

    # send data to autobox
    sent = sock.sendto(_data, _address)
    print " [-] gone: {} byte, msg: {}" .format(sent ,data_notpacked)

    time.sleep(0.1)
    print " --------------------------------------- "
