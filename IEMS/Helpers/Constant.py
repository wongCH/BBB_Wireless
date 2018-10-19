import time
from datetime import datetime
import json
class Constant:
    """
    All the Global variable are stored here for sharing with other classes
    """
    SENSOR_WORKING = True
    IS_BLUETOOTH_CONNECTED = False

    #Sensor Sleep time
    SNR_SLEEP = 0.02
    
    #current millisecond
    CURRENT_TIME =   int(time.time() * 1000)
     

    #for MQTT
    MQTT_BROKER ="iot.eclipse.org"
    MQTT_PORT = 1883
    MQTT_TOPIC = "sg/lift"
    MQTT_QOS = 0

    #file path for storing sensor data
    #FILE_STORE_NAME= "/home/debian/pythonapp/Logs/sensorData_" + datetime.utcnow().strftime('%Y-%m-%d')+'.json'
    FILE_STORE_NAME= "/sdcard/iems/Logs/sensorData_" + datetime.utcnow().strftime('%Y-%m-%d')+'.json'

    #json format for interface return json object
    INTERFACE_JSON = {"deviceId":"len_123456","created":None,"lux":0,"tem":0,"hum":0,"pre":0,"gyr": {"x":0,"y":0,"z":0},"acc":{"x":0,"y":0,"z":0}}
    
    #reading record before store and send to mqtt
    #use in SensorMGR
    MSG_COUNT= 200