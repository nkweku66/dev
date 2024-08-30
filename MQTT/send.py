import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to broker")
        global Connected
        Connected = True
    else:
        print("Connection failed")

Connected = False
client = mqtt.Client()
client.on_connect = on_connect
client.connect("mqtt.eclipseprojects.io", 1883, 60)
client.loop_start()

while Connected != True:
    time.sleep(0.1)
try:
    while True:
        topic = input('Enter topic: ')

        if topic == 'register':
             message = input('Your message: ')
             client.publish(f"glblcd/{topic}", message)
        elif topic == 'lightbulb':
            message = input('Your message: ')
            client.publish(f"glblcd/{topic}", message)
        else:
            message = input('Your message: ')
            client.publish(f"glblcd/{topic}", message)

except KeyboardInterrupt:
    client.disconnect()
    client.loop_stop()
