import time
from datetime import datetime
class Constant:
    """
    All the Global variable are stored here for sharing with other classes
    """
    SENSOR_WORKING = True
    IS_BLUETOOTH_CONNECTED = False

    #Sensor Sleep time
    SNR_SLEEP = 2
    
    #current millisecond
    CURRENT_TIME =   int(time.time() * 1000)
    STR_CURRENT_DATE_TIME =  datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]

    #for MQTT
    MQTT_BROKER = "iot.eclipse.org"
    MQTT_PORT = 1883
    MQTT_TOPIC = "sg/lift"
    MQTT_QOS = 0

    #file path for storing sensor data
    FILE_STORE_NAME= "/home/debian/pythonapp/Logs/sensorData_" + datetime.utcnow().strftime('%Y-%m-%d')+'.json'
    