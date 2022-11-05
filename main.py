
import sys
from asyncio import set_event_loop_policy, run, gather, sleep, WindowsSelectorEventLoopPolicy
if (sys.path[len(sys.path)-1] != "C:\\Users\\ajstone\\Documents\\My Games\\Roboco\\st0nerhat\\Scripts"):
    sys.path.append("C:\\Users\\ajstone\\Documents\\My Games\\Roboco\\st0nerhat\\Scripts")
import importlib
import framework.core
import local.input
import local.output
importlib.reload(framework.core)
importlib.reload(local.input)
importlib.reload(local.output)
from framework.core import UpdateLoop
from local.input import *
from local.output import *

async def dance():
    drive.forward(10)
    await sleep(3)
    drive.pivotRight(10)
    await sleep(3)
    drive.stop()
    await sleep(2)
    drive.reverse(10)
    await sleep(2)
    drive.stop()

async def main():
    loop = UpdateLoop(0.033, 0.015)
    loop.add(leftLed)
    loop.add(rightLed)
    
    await gather(
        loop.run(),
        dance()
    )

set_event_loop_policy(WindowsSelectorEventLoopPolicy())
run(main())

