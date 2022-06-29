# Soil Moisture Sensor Wireling Example
# This example will read the print out the moisture and temperature
# Written by: Laverena Wienclaw for TinyCircuits

import tinycircuits_wireling
import time
import tinycircuits_attiny25

wireling = tinycircuits_wireling.Wireling()
wireling.selectPort(0)

attiny25 = tinycircuits_attiny25.ATtiny25()

while True:
     attiny25.readMoisture()
     attiny25.readTemp()
     print("Moisture: %.2f" % attiny25.moisture)
     print("Temp DegC: %.2f" % attiny25.temp)
     time.sleep(0.5)
