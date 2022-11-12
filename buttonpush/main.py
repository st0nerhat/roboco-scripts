import sys
from asyncio import set_event_loop_policy, run, gather, sleep, WindowsSelectorEventLoopPolicy
if (sys.path[len(sys.path)-1] != "C:\\Users\\ajstone\\Documents\\My Games\\Roboco\\st0nerhat\\Scripts"):
    sys.path.append("C:\\Users\\ajstone\\Documents\\My Games\\Roboco\\st0nerhat\\Scripts")

from controllables import Piston, TextScreen
from sensors import DistanceSensor, TouchSensor
from scriptruntime import Runtime
from importlib import reload

import framework.stream
reload(framework.stream)

from framework.stream import Mux

#Inputs
distance = DistanceSensor(0)
button = TouchSensor(1)

#Outputs
screen = TextScreen(2)
piston = Piston(3)


async def main():
    stream = Mux(distance.stream(), button.force_stream())
    screen.size = 80
    screen.horizontal_alignment = TextScreen.HorizontalAlignment.LEFT
    touchDist = float('-inf')
    minDist = float('inf')
    maxForce = float('-inf')

    while True:
        for event in stream:
            distanceVal = event[0]
            F = event[1]
            x = 0
            k = 0

            if F is not None:
                if F > 1:
                    touchDist = max(touchDist, distanceVal)
                    minDist = min(minDist, distanceVal)
                    maxForce = max(F, maxForce)
                    x = touchDist - distanceVal
                    if x > 0:
                        k = -F / x
                screen.text = "F=-kx\nF: {:.2f}\nx: {:2f}\nk: {:2f}".format(F, x, k)
        await sleep(0.033)


set_event_loop_policy(WindowsSelectorEventLoopPolicy())
run(main())