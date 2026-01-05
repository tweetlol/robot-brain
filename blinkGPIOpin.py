

import gpiozero
import time

PIN_BCM_NUMBER = 21

pin = gpiozero.OutputDevice(PIN_BCM_NUMBER)

for i in range(5):
	pin.on()

	time.sleep(1)

	pin.off()

	time.sleep(1)

pin.close()

print(f"DONE")
