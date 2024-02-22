from Bluetin_Echo import Echo
import time

TRIGGER_PIN = 17
ECHO_PIN = 27


def main():
    speed_of_sound = 315
    echo = Echo(TRIGGER_PIN, ECHO_PIN, speed_of_sound)
    samples = 1
    while True:
        result = echo.read('cm', samples)
        print(f'result {result:.2f} cm')
        time.sleep(0.1)
    echo.stop()


if __name__ == "__main__":
    main()
