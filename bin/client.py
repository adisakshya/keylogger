import socket
import sys

def send(filename):
	s = socket.socket()
	s.connect(("localhost",9999))
	f = open (filename, "rb")
	l = f.read(1024)
	while (l):
	    s.send(l)
	    l = f.read(1024)
	s.close()
