from typing import List
import importlib
import framework.behaviors.wheel
importlib.reload(framework.behaviors.wheel)
from framework.behaviors.wheel import Wheel
from framework.core import IFixedUpdateable

class FourWD(IFixedUpdateable):
    lfWheel: Wheel
    rfWheel: Wheel
    lrWheel: Wheel
    rrWheel: Wheel
    allWheels: List[Wheel]
    leftWheels: List[Wheel]
    rightWheels: List[Wheel]

    def __init__(self, lfWheel:Wheel, rfWheel:Wheel, lrWheel:Wheel, rrWheel:Wheel):
        self.lfWheel = lfWheel
        self.rfWheel = rfWheel
        self.lrWheel = lrWheel
        self.rrWheel = rrWheel
        self.allWheels = [lfWheel, rfWheel, lrWheel, rrWheel]
        self.leftWheels = [lfWheel, lrWheel]
        self.rightWheels = [rfWheel, rrWheel]

    def forward(self, linearSpeed:float):
        for wheel in self.allWheels:
            wheel.spin(linearSpeed)

    def reverse(self, linearSpeed:float):
        for wheel in self.allWheels:
            wheel.spin(-linearSpeed)

    def stop(self):
        for wheel in self.allWheels:
            wheel.stop()

    def forwardLeft(self, linearSpeed:float):
        # This is a fake solution. We want to be able to have the left wheels spin freely
        for wheel in self.leftWheels:
            wheel.stop()

        for wheel in self.rightWheels:
            wheel.spin(linearSpeed)

    def forwardRight(self, linearSpeed:float):
        for wheel in self.rightWheels:
            wheel.stop()
            
        for wheel in self.leftWheels:
            wheel.spin(linearSpeed)

    def reverseLeft(self, linearSpeed:float):
        for wheel in self.leftWheels:
            wheel.stop()

        for wheel in self.rightWheels:
            wheel.spin(-linearSpeed)

    def reverseRight(self, linearSpeed:float):
        for wheel in self.rightWheels:
            wheel.stop()

        for wheel in self.leftWheels:
            wheel.spin(-linearSpeed)

    def pivotLeft(self, linearSpeed:float):
        for wheel in self.leftWheels:
            wheel.spin(-linearSpeed)

        for wheel in self.rightWheels:
            wheel.spin(linearSpeed)

    def pivotRight(self, linearSpeed:float):
        for wheel in self.rightWheels:
            wheel.spin(-linearSpeed)

        for wheel in self.leftWheels:
            wheel.spin(linearSpeed)