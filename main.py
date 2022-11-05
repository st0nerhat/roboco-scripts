
import sys
if (sys.path[len(sys.path)-1] != "C:\\Users\\ajstone\\Documents\\My Games\\Roboco\\st0nerhat\\Scripts"):
    sys.path.append("C:\\Users\\ajstone\\Documents\\My Games\\Roboco\\st0nerhat\\Scripts")
import importlib
import framework.loop
import local.input
import local.output
importlib.reload(framework.loop)
importlib.reload(local.input)
importlib.reload(local.output)
from framework.loop import loop
from local.input import *
from local.output import *


def main():
    while True:
        loop.update()

main()

