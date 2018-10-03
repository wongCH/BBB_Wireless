import Adafruit_GPIO.I2C as I2C
from Sensors.BaseSensor import *
import datetime
import binascii

import ctypes
#readResult = []
#sensorConfig = { "interface":None,"bitSize": None,"i2c": None}


class LightSensors(BaseSensor):
    """
    Reading from Light Sensors
    I2C address= 0x47
    busNum=2
    interface =must be None,else Adafruit will replace it with default busno=1
    bitSize =2 (7bit)    
    """
 

    def __init__(self, deviceAddr=0x47, busNum=2,interface=None, bitSize=10):
       super().__init__(deviceAddr,busNum,interface,bitSize)
       Device = I2C.Device(address=0x47,busnum=2)
       Device.writeList(0x01,bytearray(b'\xc4\x10'))  #configure the mode (refer to datasheet configuration table)
        #0x01 - config adr
        #0xc4 - full scale, 100ms conv. time, contiue measuring
        #0x10 - latch
       

    def getSensors(self):
        device = I2C.get_i2c_device(0x47,2)#get the i2c address on busNo2
        rawValue = device.readList(0x00,2) #return as 2bytes
        iData = (rawValue[0] << 8) | rawValue[1];
        luxResult = self.convertToLux(iData)
        #print("Lux:{0}".format(luxResult))
        return luxResult

    def convertToLux(self,rawValue):
        iMantissa = rawValue & 0x0FFF;                 # Extract Mantissa
        iExponent = (rawValue & 0xF000) >> 12;         # Extract Exponent 
        return iMantissa * (0.01 * pow(2, iExponent)); 
        #return 10