
# CONTROLS 74HC595 SWITCH REGISTER CHIP (8-BIT SERIAL INPUT / PARALLEL OUTPUT)

import gpiozero
import time

print("running fancyGPIOpins.py")

PIN_BCM_NUMBER_1 = 21
PIN_BCM_NUMBER_2 = 1
PIN_BCM_NUMBER_3 = 25

data = gpiozero.OutputDevice(PIN_BCM_NUMBER_1)
clock = gpiozero.OutputDevice(PIN_BCM_NUMBER_2)
latch = gpiozero.OutputDevice(PIN_BCM_NUMBER_3)

def ping(pin):
    pin.on()
    time.sleep(.25)
    pin.off()

time.sleep(3)
print("pinging NOW")
ping()


data.close()
clock.close()
latch.close()

print(f"DONE")
