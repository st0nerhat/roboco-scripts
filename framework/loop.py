from typing import List
from time import monotonic, sleep


class IUpdateable:
    def __init__(self):
        pass

    def update(self, dt:float):
        raise Exception("Not implemented")

class IFixedUpdateable:
    def __init__(self):
        pass

    def updateFixed(self, dt:float):
        raise Exception("Not implemented")

class UpdateLoop:
    updateList: List[IUpdateable]
    fixedUpdateList: List[IFixedUpdateable]
    startTime: float
    elapsedTime: float
    lastTime: float
    fixedUpdateRemainder: float

    def __init__(self, targetTimeStep:float, fixedTimeStep:float):
        self.targetTimeStep = targetTimeStep
        self.fixedTimeStep = fixedTimeStep
        self.updateList = []
        self.fixedUpdateList = []
        self.startTime = self.lastTime = monotonic()
        self.elapsedTime = 0
        self.fixedUpdateRemainder = 0

    def add(self, updateable:IUpdateable):
        self.updateList.append(updateable)

    def remove(self, updateable:IUpdateable):
        raise Exception("Not implemented")

    def addFixed(self, updateable:IFixedUpdateable):
        self.fixedUpdateList.append(updateable)

    def removeFixed(self, updateable:IFixedUpdateable):
        raise Exception("Not implemented")

    def update(self):
        print("update")
        start = monotonic()
        dt = start - self.lastTime
        self.elapsedTime += dt
        self.lastTime = start

        # Do regular update
        for updateable in self.updateList:
            updateable.update(dt)

        # Update fixed time steps
        fixedUpdateTotalDt = dt + self.fixedUpdateRemainder
        while fixedUpdateTotalDt >= self.fixedTimeStep:
            fixedUpdateTotalDt -= self.fixedTimeStep
            self._fixedUpdate()

        self.fixedUpdateRemainder = fixedUpdateTotalDt

        end = monotonic()
        loopTime = end - start
        sleepTime = self.targetTimeStep - loopTime

        # Sleep until target time step
        sleep(sleepTime)

    def _fixedUpdate(self):
        for updateable in self.fixedUpdateList:
            updateable.update(self.fixedTimeStep)
        
loop = UpdateLoop(0.033, 0.015)