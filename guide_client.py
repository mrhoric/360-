#!/usr/bin/python
import socket,sys

bufsize = 1024

s = socket.socket()
s.connect((sys.argv[1],int(sys.argv[2])))

while 1:
    data = raw_input('$ ')
    if not data:
        break;
    s.send(data)
    print s.recv(bufsize)

s.close()
