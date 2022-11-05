
import sys
if (sys.path[len(sys.path)-1] != "C:\\Users\\ajstone\\Documents\\My Games\\Roboco\\st0nerhat\\Scripts"):
    sys.path.append("C:\\Users\\ajstone\\Documents\\My Games\\Roboco\\st0nerhat\\Scripts")
import importlib
import framework.core.loop
import local.input
import local.output
importlib.reload(framework.core.loop)
importlib.reload(local.input)
importlib.reload(local.output)
from framework.core.loop import UpdateLoop
from local.input import *
from local.output import *


def main():
    loop = UpdateLoop(0.033, 0.015)
    loop.add(leftLed)
    loop.add(rightLed)
    
    while True:
        loop.update()

main()

