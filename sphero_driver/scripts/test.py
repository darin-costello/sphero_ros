#!/usr/bin/python
import bluetooth
import struct
import time
import sys
from sphero_driver import Sphero
sphero = Sphero()
sphero.connect()
sphero.set_raw_data_strm(40, 1 , 0, False)

sphero.start()
for i in xrange(0, 200):
    for x in xrange(0, 255):
        time.sleep(0.01)
        sphero.set_rgb_led(255-x,x,0,0,False)

    for x in xrange(0, 255):
        time.sleep(0.01)
        sphero.set_rgb_led(0,255-x,x,0,False)

    for x in xrange(0, 255):
        time.sleep(0.01)
        sphero.set_rgb_led(x,0,255-x,0,False)

sphero.join()
sphero.disconnect()
sys.exit(1)



