from gpiozero import MCP3008
from time import sleep


def main():
    print("Starting ADC test")
    while True:
        pot = MCP3008(0)
        print(pot.value)
        sleep(0.1)


if __name__ == "__main__":
    main()
