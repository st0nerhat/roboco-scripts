from controllables import DCMotor, Piston, TextScreen, LED
import importlib
import framework.behaviors.blink
import framework.behaviors.fourwd
importlib.reload(framework.behaviors.blink)
importlib.reload(framework.behaviors.fourwd)
from framework.behaviors.blink import Blink
from framework.behaviors.fourwd import FourWD

lfWheel = DCMotor(0)
rfWheel = DCMotor(3)
lrWheel = DCMotor(1)
rrWheel = DCMotor(2)

drive = FourWD(lfWheel, rfWheel, lrWheel, rrWheel)

sensorRotor = DCMotor(9)
sensorTower = Piston(8)

screen = TextScreen(5)

leftLed = Blink(LED(7))
rightLed = Blink(LED(6))