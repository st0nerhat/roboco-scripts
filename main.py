import sys
if (sys.path[len(sys.path)-1] != "C:\\Users\\ajstone\\Documents\\My Games\\Roboco\\st0nerhat\\Scripts"):
    sys.path.append("C:\\Users\\ajstone\\Documents\\My Games\\Roboco\\st0nerhat\\Scripts")
    
from framework.loop import loop
from local.input import *
from local.output import *


def main():
    print(sys.path)
    while True:
        loop.update()

main()

