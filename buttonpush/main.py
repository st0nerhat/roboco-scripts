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

    while True:
        for event in stream:
            print(event)
        await sleep(0.033)


set_event_loop_policy(WindowsSelectorEventLoopPolicy())
run(main())