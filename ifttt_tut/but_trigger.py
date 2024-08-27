from gpiozero import LED, Button
from signal import pause
import requests


# led = LED(17)
button = Button(17)

def request():
    print("Sending")
    response = requests.get("https://maker.ifttt.com/trigger/Button_pressed/with/key/wXibIBusz16iQXQT8VBnq")
    if response.status_code == 200:
        print("Hell yeah am on")

button.when_pressed = request

pause()