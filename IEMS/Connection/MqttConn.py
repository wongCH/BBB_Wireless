import paho.mqtt.client  
import paho.mqtt.publish
import json
class MqttConn(object):
    """description of class"""
    
    BROKER = "hnas.dnet.com.sg"
    PORT = 1883
    TOPIC = "iems/sg/lift/condition"
    CLIENT_ID = "MQTT_Client"
    def publish(self,sectime,light,temp,humidity,preasure,gyro_x,gyro_y,gyro_z,acc_x,acc_y,acc_z):
        x =[
             {"resource":"light","data":light, "ts":sectime },
             {"resource":"temperature","data":temp, "ts":sectime },
             {"resource":"humidity","data":humidity,"ts":sectime },
             {"resource":"pressure","data":preasure,"ts":sectime },
             {"resource":"gyro_x","data":gyro_x,"ts":sectime } ,
             {"resource":"gyro_y","data":gyro_y,"ts":sectime } ,
             {"resource":"gyro_z","data":gyro_z,"ts":sectime } ,
             {"resource":"acc_x","data":acc_x,"ts":sectime } ,
             {"resource":"acc_y","data":acc_y,"ts":sectime } ,
             {"resource":"acc_z","data":acc_z,"ts":sectime } 
        ]
        json_data =json.dumps(x);
        
        paho.mqtt.publish.single(
		topic=self.TOPIC,
		payload="hello",
		qos=0,
		hostname=self.BROKER,
		port=self.PORT,
		client_id=self.CLIENT_ID
		)
        print ("send time:{0}".format(sectime))

  