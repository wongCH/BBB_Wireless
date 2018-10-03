import paho.mqtt.client  as mqtt
 
import json
class MqttConn(object):
    """description of class"""
    
    BROKER = "hnas.dnet.com.sg"
    PORT = 1883
    TOPIC = "iems/sg/lift/condition"
    CLIENT_ID = "lens_dblXiL0qkIW5o5NG2EtWbgqJZuw"

    def __init__(self):
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client._client_id = self.CLIENT_ID
        self.client.connect(self.BROKER, self.PORT, 60)
        self.client.loop_start()

    def on_connect(self,client, data, rc):
       self.client.subscribe("IEMS/light", 1) #QoS=1
       print(rc)#get server status

    def on_message(self,client, data, msg):
        print(msg.topic + " " + str(msg.payload))
        

    def publish(self,sectime,light,temp,humidity,preasure,gyro_x,gyro_y,gyro_z,acc_x,acc_y,acc_z):
      
        self.client.publish(topic=self.TOPIC,payload="Hello from Wong", qos=0)
        print ("send time:{0}".format(sectime))

  