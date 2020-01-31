from Adafruit_BME280 import *
from time import sleep
from datetime import datetime
import paho.mqtt.publish as publish
sensor = BME280(t_mode=BME280_OSAMPLE_8, p_mode=BME280_OSAMPLE_8, h_mode=BME280_OSAMPLE_8)
MQTT_SERVER = "10.191.12.3"
MQTT_PATH = "test_channel"

while True:
    
    file1=open("weatherlog.txt","a")
    degrees = sensor.read_temperature()
    humidity = sensor.read_humidity()
    pascals = sensor.read_pressure()
    KPA = (pascals) / 1000
    Faren = (degrees*9/5)+32
    now = datetime.now()
    dt_string = now.strftime("%m/%d/%Y-%H:%M:%S ")
    file1.write(dt_string)
    print (dt_string)
    
    print 'Temp      = {0:0.3f}'.format(Faren)
    print 'Humidity  = {0:0.6f}'.format(humidity)
    print 'Pressure  = {0:0.4f}'.format(KPA)
    
    publish.single("Temp(P)", Faren, hostname=MQTT_SERVER)
    publish.single("Pressure(P)", KPA, hostname=MQTT_SERVER)
    publish.single("Humidity(P)", humidity, hostname=MQTT_SERVER)
    
    file1.write('Temp= {0:0.3f}F '.format(Faren) )
    file1.write(' Humidity= {0:0.6f}%'.format(humidity) )
    file1.write(' Pressure= {0:0.4f}inHg \n'.format(KPA))
    
    sleep(5)
   
    