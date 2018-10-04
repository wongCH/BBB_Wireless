#! /usr/bin/python
#
# Title:perky_blue.py
# Description:
# Development Environment:OS X 10.9.3/Python 2.7.7
# Author:G.S. Cole (guycole at gmail dot com)
#
from bluetooth import *
import time
import threading


class Bluetooth:

    def Execute(self,liSnr):
        service_uuid = "00001101-0000-1000-8000-00805F9B34FB"
        server_sock = BluetoothSocket(RFCOMM)
        server_sock.bind(("", PORT_ANY))
        server_sock.listen(1)

        port = server_sock.getsockname()[1]

        advertise_service(server_sock, "PerkyBlue", service_id = service_uuid, service_classes = [service_uuid, SERIAL_PORT_CLASS], profiles = [SERIAL_PORT_PROFILE])

        print("awaiting RFCOMM connection on channel:%d" % port)

        client_sock, client_info = server_sock.accept()
        print("accepted connection from:", client_info)

        try:
            while True:
                #data = client_sock.recv(1024).strip()
                
                while True:
                    client_sock.sendall("Lux:"+ str(liSnr.getSensors())+"\n")
                    time.sleep(2)

        except IOError:
            pass

        print("disconnected")

        #client_sock.close()
        #server_sock.close()
        print("all done")
    def Main(self,liSnr,imuSnr,envSnr):
        service_uuid = "00001101-0000-1000-8000-00805F9B34FB"
        server_socket=BluetoothSocket(RFCOMM)
        server_socket.bind(("",1))
        server_socket.listen(1)
        advertise_service(server_socket, "IEMSBlue", service_id = service_uuid, service_classes = [service_uuid, SERIAL_PORT_CLASS], profiles = [SERIAL_PORT_PROFILE])

        while True:
            sock,info=server_socket.accept()
            print(str(info[0])+'Connected!')
            t=threading.Thread(target=self.serveSocket,args=(sock,liSnr,envSnr,))
            t.setDaemon(True)
            t.start()
    server_socket=None
    def serveSocket(self,sock,liSnr,envSnr):
      
        try:
           
            while True:
                envData =envSnr.getSensors()
                strSend="Lux:{0},Temp:{1}".format(str(liSnr.getSensors()),envData['temp'])
                sock.sendall(strSend+"\n")
                time.sleep(0.2)
        except Exception as e:
             pass
             print ("erorr:" + e.message )
      
        finally:
             sock.close()
             
        print("close connection")
        
        