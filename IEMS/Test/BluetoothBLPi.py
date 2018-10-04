#!/usr/bin/python3

from bluetooth import *
import threading


#Server socket (used to receive new links)
server_socket=None

#connect socket service sub-thread
def serveSocket(sock,info):
    #Open an infinite loop waiting for the client to send a message
    while True:
        #Receive 1024 bytes, then decode in UTF-8 (Chinese) 
        #automatically block thread (API) if there is no information to receive
        receive = sock.recv(1024).decode('utf-8')
        # Print what you just received (info=address)
        print('['+str(info)+']'+receive)
        #add a new line
        receive=receive+"\n"
        #Return data to the sender
        sock.send(receive.encode('utf-8'));


#Main Thread

#Create a server socket to listen on the port

server_socket=BluetoothSocket(RFCOMM);

#Allow host connection of any address, unknown parameters: 1 (port number, channel number)
server_socket.bind(("",1))

#Listening port/channel
server_socket.listen(1)

#Open loop waiting for client connection
port = server_socket.getsockname()[1]
service_uuid = "00001101-0000-1000-8000-00805F9B34FB"

#advertise_service(server_socket, "IemsServer", service_id = service_uuid, service_classes = [service_uuid, SERIAL_PORT_CLASS], profiles = [SERIAL_PORT_PROFILE])

print("awaiting RFCOMM connection on channel:%d" % port)
        
advertise_service(server_socket, "BeagleBone", service_id = service_uuid, service_classes = [service_uuid, SERIAL_PORT_CLASS], profiles = [SERIAL_PORT_PROFILE])
      
#This place should be placed in another sub-thread

while True:
    #Waiting for someone to connect, if no one connect,
    #block the thread waiting (this would have to be a session pool
    #to facilitate sending data to different devices)
    
    sock,info=server_socket.accept()
    #Print a message that someone has connected
    print(str(info[0])+'Connected!')
    #Create a thread dedicated to the new connection 
    #(this should have a thread pool to manage the thread)
    t = threading.Thread(target=serveSocket,args=(sock,info[0]))
    
    #Set the thread guard to prevent the program from 
    #ending before the thread ends
    
    t.setDaemon(True)
    print("Starting the thread")
    #Start thread
    t.start();

#本文来自 hehung 的CSDN 博客 ，全文地址请点击：https://blog.csdn.net/hehung/article/details/78159176?utm_source=copy 
"""
1. Install the following
sudo apt-get installPython-dev

sudo apt-get install libbluetooth-dev
sudo pip3 install pybluez

2. in terminal:
$ bluetoothctl
[bluetooth]# discoverable yes
"""