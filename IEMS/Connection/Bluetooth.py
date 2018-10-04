#!/usr/bin/python3
#
# Title:perky_blue.py
# Description:
# Development Environment:OS X 10.9.3/Python 2.7.7
# Author:G.S. Cole (guycole at gmail dot com)
#
 

from bluetooth import *
from Helpers.Constant import *


from threading import Thread
 
class IemsServer(Thread):
    def __init(self):
        print("Start")
    def toggleLed(self, target):
        print(target)
        if (target == 'green'):
            print ('toggle green')
        elif (target == 'red'):
            print ('toggle red')
        elif (target == 'yellow'):
            print ("Yellow")		 
        else:
            print ('unknown remote command')

    def Main(self):
        print ('Bluetooth Server Start')
        service_uuid = "00001101-0000-1000-8000-00805F9B34FB"
        
    
        server_sock = BluetoothSocket(RFCOMM)
        server_sock.bind(("", PORT_ANY))
        server_sock.listen(1)

        port = server_sock.getsockname()[1]

        advertise_service(server_sock, "IemsServer", service_id = service_uuid, service_classes = [service_uuid, SERIAL_PORT_CLASS], profiles = [SERIAL_PORT_PROFILE])

        print("awaiting RFCOMM connection on channel:%d" % port)
        

        self.client_sock,self.client_info = server_sock.accept()
        print("accepted connection from:", self.client_info)
        #start sending Message
        Constant.IS_BLUETOOTH_CONNECTED = True
        self.SendMessageTo("Start Streaming")

        try:
            while True:
                data =self.client_sock.recv(1024).strip()
                if len(data) == 0: break
                print("received [%s]" % data)
                self.client_sock.sendall('OK')

                self.toggleLed(data)
        except IOError:
            Constant.IS_BLUETOOT_CONNECTED = false
            pass
        print("disconnected")

        client_sock.close()
        server_sock.close()
        print("all done")
        
    def SendMessageTo(self,message):
        self.client_sock.sendall(message)
  
 