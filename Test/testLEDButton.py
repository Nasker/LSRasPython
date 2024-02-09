from gpiozero import Button
from gpiozero import LED


def main():
    print("Starting LED and Button test")
    button_pin = 21
    led_pin = 20
    print("Button pin: " + str(button_pin))
    print("LED pin: " + str(led_pin))

    button = Button(button_pin)
    led = LED(led_pin)

    while True:
        if button.is_pressed:
            led.on()
        else:
            led.off()


if __name__ == "__main__":
    main()
