

import gpiozero
import time

PIN_BCM_NUMBER_1 = 21
PIN_BCM_NUMBER_2 = 1

pin1 = gpiozero.OutputDevice(PIN_BCM_NUMBER_1)
pin2 = gpiozero.OutputDevice(PIN_BCM_NUMBER_2)

for i in range(6):
	pin1.on()
	time.sleep(.5)
	pin1.off()
	pin2.on()
	time.sleep(.5)
	pin2.off()
pin1.off()


for i in range(6):
	pin1.on()
	pin2.on()
	time.sleep(1/i)

for i in range(6):
	pin1.on()
	time.sleep(.5)
	pin1.off()
	pin2.on()
	time.sleep(.5)
	pin2.off()
pin1.off()



pin1.close()
pin2.close()

print(f"DONE")
