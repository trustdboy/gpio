from gpiozero import LED
from time import sleep

led = LED(17)

def dot():
	led.on()
	sleep(0.01)
	led.off()
	sleep(1)

def name():
	led.on()
	sleep(1)
	led.off()
	sleep(0.01)

def dash():
	led.on()
	sleep(0.01)
	led.off()
	sleep(2)

dot()
dot()
name()
dash()
dash()
dot()
dot()
name()
dash()
dash()
dot()
dot()
name()
dash()
dash()
dot()
dot()
