mqttServer="iot.eclipse.org"
mqttPort=1883

channelSubs="sg/lift" #topic configure as as index in ES

import paho.mqtt.client as mqtt
from datetime import datetime
from elasticsearch import Elasticsearch
es = Elasticsearch() #[{'host': 'localhost', 'port': 9200}]

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(channelSubs)

def on_message(client, userdata, msg):
    #print(msg.topic+" "+str(msg.payload))
    try:
        doc = {
             'author': 'kimchy',
            'text': 'Elasticsearch: cool. bonsai cool.',
            'timestamp': datetime.now(),
        }

	    #print(msg.payload)
        es.index(index="sg", doc_type="external", body=msg.payload)
        res = es.index(index=channelSubs, doc_type='tweet', id=1, body=doc)
        print(res['result'])
    	
    except:
        prin("Error")
	#es.index(index="my-index", doc_type="string", body={"topic" : msg.topic, "dataString" : msg.payload, "timestamp": datetime.utcnow()})

client = mqtt.Client("imes-sevr-01")
client.on_connect = on_connect
client.on_message = on_message
client.connect(mqttServer,mqttPort, 60)
client.loop_forever()
print("subscribing ")
client.subscribe(channelSubs)#subscribe

s