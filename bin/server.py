import socket
import sys
s = socket.socket()
s.bind(("localhost",9999))
s.listen(10)
i = 0
print('listening on port: 9999')
while True:
    sc, address = s.accept()

    print('Got connection from: ',address)
    f = open('new_'+ str(i)+".txt",'wb') #open in binary
    i=i+1
    while (True):
        l = sc.recv(1024)
        f.write(l)
        """
        while (l):
                f.write(l)
                l = sc.recv(1024)
        """        
    f.close()


    sc.close()

s.close()
