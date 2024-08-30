import paho.mqtt.client as mqtt
from gpiozero import LED
from time import sleep

led = LED(17)

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    client.subscribe("glblcd/lightbulb")
    client.subscribe("glblcd/register")
    client.subscribe("glblcd/Kod")

def on_message(client, userdata, msg):
    if msg == "on":
        led.on()
        print('Light')
        sleep(1)
    elif msg == "off":
        led.off()
        sleep(0)
    print(msg.topic + " \n " + msg.payload.decode("utf-8") + " \n ")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("mqtt.eclipseprojects.io", 1883, 60)
client.loop_forever()
