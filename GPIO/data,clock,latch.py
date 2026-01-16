
# CONTROLS 74HC595 SWITCH REGISTER CHIP (8-BIT SERIAL INPUT / PARALLEL OUTPUT)

import gpiozero
import time

print("data,clock,latch.py")

PIN_BCM_NUMBER_1 = 21
PIN_BCM_NUMBER_2 = 1
PIN_BCM_NUMBER_3 = 25

data = gpiozero.OutputDevice(PIN_BCM_NUMBER_1)
clock = gpiozero.OutputDevice(PIN_BCM_NUMBER_2)
latch = gpiozero.OutputDevice(PIN_BCM_NUMBER_3)

data.off()
clock.off()
latch.off()

SLEEPS = 0.01

def ping(pin):
    time.sleep(SLEEPS)
    pin.on()
    time.sleep(SLEEPS)
    pin.off()
    
def write(bit):
    if bit == 1:
        data.on()
        ping(clock)
        data.off()
    elif bit == 0:
        ping(clock)
    else:
        print("ERROR: non-binary written value")

def fill(bit):
    if bit == 1:
        data.on()
        for i in range(8):
            ping(clock)
        data.off()
    elif bit == 0:
        data.off()
        for i in range(8):
            ping(clock)
    else:
        print("ERROR: non-binary written value")

fill(0)
ping(latch)

for i in range(100):
    write(i%2)
    ping(latch)

data.close()
clock.close()
latch.close()

print(f"DONE")
