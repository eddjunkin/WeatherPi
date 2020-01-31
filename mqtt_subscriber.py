import paho.mqtt.client as mqtt
from datetime import datetime
MQTT_SERVER = "localhost"
 
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
 
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("Temp(P)")
    client.subscribe("Humidity(P)")
    client.subscribe("Pressure(P)")
    client.subscribe("Temp(R)")
    client.subscribe("Humidity(R)")
    client.subscribe("Pressure(R)")
    
 
# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    # (P) denotes Purple sensor working. 
    if msg.topic == "Temp(P)" or "Pressure(P)" or "Humidity(P)":
        file1=open("DataLog(P).txt","a")
        if msg.topic == "Temp(P)":
            now = datetime.now()
            dt_string = now.strftime("%m/%d/%Y-%H:%M:%S ")
            file1.write(dt_string)
            file1.write(msg.payload)
            
            print (dt_string)
            print (msg.topic+"     "+str(msg.payload))
        if msg.topic == "Pressure(P)":
            file1.write(" "+msg.payload)
            print (msg.topic+" "+str(msg.payload))
        if msg.topic == "Humidity(P)":
            
            file1.write(" "+msg.payload)
            print (msg.topic+" "+str(msg.payload))
            file1.write('\n')
            
            
    if msg.topic == "Temp(R)" or "Pressure(R)" or "Humidity(R)":
        file1=open("DataLog(R).txt","a")
        if msg.topic == "Temp(R)":
            now = datetime.now()
            dt_string = now.strftime("%m/%d/%Y-%H:%M:%S ")
            file1.write(dt_string)
            file1.write(msg.payload)
            
            print (dt_string)
            print (msg.topic+"     "+str(msg.payload))
        if msg.topic == "Pressure(R)":
            file1.write(" "+msg.payload)
            print (msg.topic+" "+str(msg.payload))
        if msg.topic == "Humidity(R)":
            
            file1.write(" "+msg.payload)
            print (msg.topic+" "+str(msg.payload))
            file1.write('\n')
        
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
 
client.connect(MQTT_SERVER, 1883, 60)
 
# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
