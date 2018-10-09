mqttServer="iot.eclipse.org"
mqttPort=1883
channelSubs="sg/lift" #mqtt topc

import paho.mqtt.client as mqtt
from datetime import datetime
from elasticsearch import Elasticsearch
es = Elasticsearch() #[{'host': 'localhost', 'port': 9200}]

#create index mapping
mappings = {
        'lift': {
            'properties': {
                'deviceId': {'type': 'text'},             
                'created': {'type': 'date'},
                'lux': {'type': 'integer'},
                'tem': {'type': 'integer'},
                'hum': {'type': 'integer'},
                'pre': {'type': 'integer'},
                'acc.x': {'type': 'integer'},
                'acc.y': {'type': 'integer'},
                'acc.z': {'type': 'integer'},
                'gyr.x': {'type': 'integer'},
                'gyr.y': {'type': 'integer'},
                'gyr.z': {'type': 'integer'}
               }
        }
    }
body = {'mappings': mappings}

if not es.indices.exists(index="sg") :
    es.indices.create(index="sg",body=body)
    print('created index')

######  MQTT Connection ######

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(channelSubs)

def on_message(client, userdata, msg):
    #print(msg.topic+" "+str(msg.payload))
    try:
        print(msg.payload)
        res = es.index(index="sg", doc_type="lift", body=msg.payload)
        print(res['result'])
    except Exception as ex:
        print("Error" + ex.message)
	#es.index(index="my-index", doc_type="string", body={"topic" : msg.topic, "dataString" : msg.payload, "timestamp": datetime.utcnow()})
 
client = mqtt.Client("imes-sevr-01")
client.on_connect = on_connect
client.on_message = on_message
client.connect(mqttServer,mqttPort, 60)
client.loop_forever()
print("subscribing ")
client.subscribe(channelSubs)#subscribe