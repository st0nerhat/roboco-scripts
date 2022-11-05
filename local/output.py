from controllables import DCMotor, Piston, TextScreen, LED
import importlib
import framework.behaviors.blink
import framework.behaviors.fourwd
importlib.reload(framework.behaviors.blink)
importlib.reload(framework.behaviors.fourwd)
from framework.behaviors.wheel import Wheel
from framework.behaviors.blink import Blink
from framework.behaviors.fourwd import FourWD

lfWheel = Wheel(DCMotor(0), 3/2)
rfWheel = Wheel(DCMotor(3), 3/2)
lrWheel = Wheel(DCMotor(1), 3/2)
rrWheel = Wheel(DCMotor(2), 3/2)

drive = FourWD(lfWheel, rfWheel, lrWheel, rrWheel)

sensorRotor = DCMotor(9)
sensorTower = Piston(8)

screen = TextScreen(5)

leftLed = Blink(LED(7))
rightLed = Blink(LED(6))