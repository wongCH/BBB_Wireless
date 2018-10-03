"""
 Sensor Model : BME280
"""
import Adafruit_GPIO.I2C as I2C
from Sensors import BME280
from Sensors.BaseSensor import *
from enum import Enum

from Sensors.BME280 import *


class EnvironmentalSensor(BaseSensor):
    """
        This class is to defined BMP280 sensors configuration and also settings
    """
     
    #I2C Address/BITS/Settings
    __BMP280_ADDRESS = 0x77
    __BMP280_CHIPID  = 0x58
    __BBB_BUSNO      = 2
    __BMP280_BITSIZE = 2
    #Registers                  

    
    def __init__(self):
        super().__init__( self.__BMP280_ADDRESS, self.__BBB_BUSNO, None, self.__BMP280_BITSIZE)
        self.getSensors()

    def getSensors(self):
        device = I2C.get_i2c_device(0x77,2)
        bme = BME280()
        t, p, h = bme.get_data()
        print ("Temperature: %f °C" % t)
        print ("Pressure: %f P" % p)
        print ("Humidity: %f %%" % h)
        