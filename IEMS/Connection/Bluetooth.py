#!/usr/bin/python3
#
# Title:perky_blue.py
# Description:
# Development Environment:OS X 10.9.3/Python 2.7.7
# Author:G.S. Cole (guycole at gmail dot com)
#
 

from Sensors.LightSensors import *
from bluetooth import *
from Helpers.Constant import *
import threading  
class Bluetooth:

   
    def Start(self,liSnr):
    	
        self.service_uuid = "00001101-0000-1000-8000-00805F9B34FB"
        self.server_sock = BluetoothSocket(RFCOMM)
        self.server_sock.bind(("", PORT_ANY))
        self.server_sock.listen(1)
        port = self.server_sock.getsockname()[1]
        advertise_service(self.server_sock, "PerkyBlue", service_id = self.service_uuid, service_classes = [self.service_uuid, SERIAL_PORT_CLASS], profiles = [SERIAL_PORT_PROFILE])
        print("awaiting RFCOMM connection on channel:%d" % port)
        
       
        while True:
            self.client_sock, self.client_info = self.server_sock.accept()
            Constant.IS_BLUETOOTH_CONNECTED = True
            print("Accepted connection from:", self.client_info)

            t = threading.Thread(target=self.ServeSocket,args=(self.server_sock,self.client_info[0], liSnr))
            t.setDaemon(True)
            print("Starting the thread")
            #Start thread
            t.start();
           
            
    def ServeSocket(self,sock,info, liSnr):
        try:
            while True:
            #Receive 1024 bytes, then decode in UTF-8 (Chinese) 
            #automatically block thread (API) if there is no information to receive
                print("inside thread")
                receive = sock.recv(1024).decode('utf-8')
            # Print what you just received (info=address)
                message =liSnr.getSensors()
                print (message)
               # print('['+str(info)+']'+liSnr.getSensors())
            #add a new line
                receive=receive+"\n"
            #Return data to the sender
              
                #sock.send(str(message));
                sock.send(receive.encode('utf-8'));
        except IOError:
             pass
        print("Disconnected")
        self.client_sock.close()
        self.server_sock.close()
        Constant.IS_BLUETOOTH_CONNECTED = False
      
    global g_message

    def SendMessageTo(self,message):
        g_message = message
 