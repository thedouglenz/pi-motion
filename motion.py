from gpiolib import *
from time import sleep

IP = 22
OP = 16

# reset the pins for use
init()

# setup pin **IP** as input and **OP** as output
set_pin_in(IP)
set_pin_out(OP)

while True:
    try:
	#print(get_input(IP))
	if(get_input(IP)):
	    trigger(OP)
	else:
	    send_low(OP)
	#sleep(0.5)
    except KeyboardInterrupt:
	cleanup()
	exit()
