CLIENT_ID ="IMES_SERVER_1"
from Helpers.Constant import *
import paho.mqtt.client as mqtt
from datetime import datetime
from elasticsearch import Elasticsearch
es = Elasticsearch() #[{'host': 'localhost', 'port': 9200}]

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(Constant.MQTT_TOPIC)

def on_message(client, userdata, msg):
    try:
        #print(msg.payload)
        res= es.index(index="sg", doc_type="sensor", body=msg.payload)
        print(res['result'])
    	
    except:
        prin("Error")
	#es.index(index="my-index", doc_type="string", body={"topic" : msg.topic, "dataString" : msg.payload, "timestamp": datetime.utcnow()})

client = mqtt.Client(CLIENT_ID)
client.on_connect = on_connect
client.on_message = on_message
client.connect(Constant.MQTT_BROKER,Constant.MQTT_PORT, 120)
client.loop_forever()
print("Subscribing ")
client.subscribe(Constant.MQTT_TOPIC)#subscribe


