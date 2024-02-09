from gpiozero import Button
from gpiozero import LED

buttonPin = 21
ledPin = 20

button = Button(buttonPin)
led = LED(ledPin)

while(True):
    if button.is_pressed:
        led.on()
    else:
        led.off()