from controllables import LED
from framework.loop import loop, IUpdateable
from color import Color
from math import sin, tau, pow

class Blink(IUpdateable):
    def __init__(self, led:LED, period=5, punchiness=4):
        self.led = led
        self.period = period
        self.time = 0
        self.punchiness = punchiness
        loop.add(self)

    def update(self, dt:float):
        #sample a sin wave with period pulse_length
        intensity = sin(loop.elapsedTime * tau / self.period)

        #put it between 0 and 1
        intensity = (1 + intensity) / 2.

        #raise intensity to a power to sharpen the curve
        intensity = pow(intensity, self.punchiness)

        self.led.color = Color(red=intensity, green=0, blue=0)