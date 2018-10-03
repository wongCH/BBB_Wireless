

import time
from time import sleep
from beebotte import *
from Helpers.Constant import *

import paho.mqtt.client as mqtt



class Beebotte:
    """description of class"""
    PORT    = 1883
    BROKER  = "mqtt.beebotte.com"
    TOKEN   = "token_WUj0OVDO4XZayZZw"
    CHANNEL = "IEMS"
    bclient = BBT('R7RlQ7zqfbg2zmFRmThAzBew','VFrNrFY3HXpIAJ81DQuusdRVApDAa8cp')
    

    def __init__(self):
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.username_pw_set("token:{0}".format(self.TOKEN))
        self.client.connect(self.BROKER, self.PORT, 60) # 60 = keepalive: Maximum period in seconds between communications with the
                                                        #broker. If no other messages are being exchanged, this controls the
                                                        #rate at which the client will send ping messages to the broker.
        self.client.loop_start()

    def on_connect(client, data, rc):
       self.client.subscribe("IEMS/light", 1) #QoS=1
       print(rc)#get server status

    def on_message(client, data, msg):
        print(msg.topic + " " + str(msg.payload))
        
    def testPublish(self):
         self.client.publish("IEMS/light", 111, 1)
         #print ("send time:{0}".format(time))

    def publish(self,sectime,light,temp,humidity,preasure,gyro_x,gyro_y,gyro_z,acc_x,acc_y,acc_z):
         self.client.publish("IEMS/light", "10", 1)
         print ("send time:{0}".format(sectime))
         self.bclient.writeBulk('IEMS', [
             {"resource":"light","data":light, "ts":sectime },
             {"resource":"temperature","data":temp, "ts":sectime },
             {"resource":"humidity","data":humidity,"ts":sectime },
             {"resource":"pressure","data":preasure,"ts":sectime },
             {"resource":"gyro_x","data":gyro_x,"ts":sectime } ,
             {"resource":"gyro_y","data":gyro_y,"ts":sectime } ,
             {"resource":"gyro_z","data":gyro_z,"ts":sectime } ,
             {"resource":"acc_x","data":acc_x,"ts":sectime } ,
             {"resource":"acc_y","data":acc_y,"ts":sectime } ,
             {"resource":"acc_z","data":acc_z,"ts":sectime } 
        ])
       
       
        #for sensor in self.objinterface['data']:
                    
           
           
"""
Data records to be published to the given channel. it Must respect the following format: 

records:[{
    resource: (string, required) name of the resource
    data: (object, required) data to be published to the resource
    ts: (integer, optional) timestamp in milliseconds

}]

   bclient.writeBulk('thing1', [
  {'resource': 'temperature', 'data': 23},
  {'resource': 'humidity', 'data': 50}
])
    {'resource': 'temperature', 'data': 23, 'ts': 1500000000000},
"""