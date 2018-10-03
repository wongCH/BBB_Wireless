
from Sensors.BaseSensor import *
import datetime
import time

ACC_FRAMES	= 10  #10 Frames are available every 100ms @ 100Hz */
GYR_FRAMES	= 10
MAG_FRAMES	= 10
"""
10 frames containing a 1 byte header, 6 bytes of accelerometer, 
 * 6 bytes of gyroscope and 8 bytes of magnetometer data. This results in
 * 21 bytes per frame. Additional 40 bytes in case sensor time readout is enabled 
"""
FIFO_SIZE =	250 
#bmi160_dev = bmi;
#bmm150_dev  = bmm;
class bmm150Test(oobject):
     #Initialize your host interface to the BMI160 */
    def __init__(self):
    #This example uses I2C as the host interface */
     bmi.id = 0x69
    #bmi.read = user_i2c_read;
    #bmi.write = user_i2c_write;
   # bmi.delay_ms = user_delay_ms;
    bmi.interface = 2

    #The BMM150 API tunnels through the auxiliary interface of the BMI160 */
    #Check the pins of the BMM150 for the right I2C address */
    bmm.dev_id =  0x13
    bmm.intf = 2
    #bmm.read = bmm150_aux_read;
    #bmm.write = bmm150_aux_write;
    #bmm.delay_ms = user_delay_ms;
