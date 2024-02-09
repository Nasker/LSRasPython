from gpiozero import MCP3008
from time import sleep

while(True):
    pot = MCP3008(0)
    print(pot.value)
    sleep(0.1)