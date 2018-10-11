mqttServer="iot.eclipse.org"
mqttPort=1883
channelSubs="sg/lift" #mqtt topc

import paho.mqtt.client as mqtt
import json
from Helpers.Compress import *
from Helpers.Constant import *

from datetime import datetime
from elasticsearch import Elasticsearch
from elasticsearch import helpers
es = Elasticsearch() #[{'host': 'localhost', 'port': 9200}]

#create index mapping
mappings = {
        'lift': {
            'properties': {
                'deviceId': {'type': 'text'},             
                'created': {'type': 'date'},
                'lux': {'type': 'float'},
                'tem': {'type': 'float'},
                'hum': {'type': 'float'},
                'pre': {'type': 'float'},
                'acc.x': {'type': 'float'},
                'acc.y': {'type': 'float'},
                'acc.z': {'type': 'float'},
                'gyr.x': {'type': 'float'},
                'gyr.y': {'type': 'float'},
                'gyr.z': {'type': 'float'}
                
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
        uncompress= Compress.GunzipBytesObj(msg.payload)
        objJson= json.loads(uncompress)
        set_es(objJson)
        
    except Exception as ex:
        print("Error" + ex.message)

#insert elasticseach
def set_es(data):
        actions = []
        #print(data["data"])
        for item in data["data"]:
            action = {"_index": "sg","_type": "lift","_source": item}
            actions.append(action)
        print (actions)
        log = helpers.bulk(es, actions)
        print(log)
 
client = mqtt.Client("imes-sevr-01")
client.on_connect = on_connect
client.on_message = on_message
client.connect(mqttServer,mqttPort, 60)
client.loop_forever()
print("subscribing ")
client.subscribe(channelSubs)#subscribe
