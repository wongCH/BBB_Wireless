import paho.mqtt.client  as mqtt
from  Helpers.Constant import *
import json

class MqttConn(object):
    """description of class"""
    CLIENT_ID = "lens_dblXiL0qkIW5o5NG2EtWbgq"
    def __init__(self):
        self.client = mqtt.Client()
        #self.username_pw_set()
        try:
            
            self.client.on_connect = self.OnConnect
            self.client.on_message = self.OnMessage
            self.client._client_id = self.CLIENT_ID
            self.client.connect(Constant.MQTT_BROKER, Constant.MQTT_PORT, 120)
            self.client.loop_start()
        except Exception as ex: 
            print("MQTT Server connection fail:" + str(ex))

    def OnConnect(self,client, data, rc):
       print("Connected to MQTT Broker:" + Constant.MQTT_BROKER)

    def OnMessage(self,client, data, msg):
        print(msg.topic + " " + str(msg.payload))
        

    def Send(self,strMessage):
        """
        send your json data 
        """
        self.client.publish(topic=Constant.MQTT_TOPIC,payload=strMessage, qos=Constant.MQTT_QOS)
        

  