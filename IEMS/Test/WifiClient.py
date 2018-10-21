#! python3 
import socket
HOST='beaglebone.local'
PORT=5002

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
while 1:
     data=s.recv(10240)
     print(data)

s.close()
