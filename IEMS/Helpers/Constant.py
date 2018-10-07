import time
class Constant:
    """
    All the Global variable are stored here for sharing with other classes
    """
    SENSOR_WORKING = True
    IS_BLUETOOTH_CONNECTED = False

    #Sensor Sleep time
    SNR_SLEEP = 0.2
    
    #current millisecond
    CURRENT_TIME =   int(time.time() * 1000)

    #for MQTT
    MQTT_BROKER = "iot.eclipse.org"
    MQTT_PORT = 1883
    MQTT_TOPIC = "sg/lift"
    MQTT_QOS = 0