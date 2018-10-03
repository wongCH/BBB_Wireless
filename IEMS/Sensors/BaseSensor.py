import Adafruit_GPIO.I2C as I2C
from abc import ABC,abstractmethod
class BaseSensor:

    """ 
        Base abstract base class to be inherit for all the sensors.
        You cannot directly call abstract class
        Parameters:
        deviceAddr : Address from I2C
        busNum : busNum from beagleBone
        interface: register address of the sensors
        bitSize: 7bits from the sensor

    """
    readResult = []
    sensorConfig = { "interface":None,"bitSize": None,"i2c": None}

    
    def __init__(self, deviceAddr, busNum,interface, bitSize):
        """
            this class initiate and inject the value into the class,implementing 
            dependency injection pattern
        """
        self.sensorConfig["interface"] = interface
        self.sensorConfig["bitSize"] = bitSize
        self.sensorConfig["i2c"] = I2C.Device(deviceAddr,busNum)
    
    @abstractmethod
    def getFrmSensor(self):
        try:
           readResult = self.sensorConfig["i2c"].readList(self.sensorConfig["interface"],self.sensorConfig["bitSize"])
           print (readResult)
           
        except TypeError as error:
            """
            to be replace to Util class to write into logs
            """
            print(error)