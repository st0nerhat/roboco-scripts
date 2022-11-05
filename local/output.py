from controllables import DCMotor, Piston, TextScreen, LED
import importlib
import framework.behaviors.blink
importlib.reload(framework.behaviors.blink)
from framework.behaviors.blink import Blink

lfWheel = DCMotor(0)
rfWheel = DCMotor(3)
lrWheel = DCMotor(1)
rrWheel = DCMotor(2)

sensorRotor = DCMotor(9)
sensorTower = Piston(8)

screen = TextScreen(5)

leftLed = Blink(LED(7))
rightLed = Blink(LED(6))