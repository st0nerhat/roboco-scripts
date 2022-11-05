from typing import List
from time import monotonic
from asyncio import sleep

class TimeStep:
    elapsed: float
    dt: float

    def __init__(self):
        self.elapsed = 0
        self.dt = 0

    def update(self, dt):
        self.elapsed += dt
        self.dt = dt

class IUpdateable:
    def __init__(self):
        pass

    def update(self, dt:TimeStep):
        raise Exception("Not implemented")

class IFixedUpdateable:
    def __init__(self):
        pass

    def updateFixed(self, dt:TimeStep):
        raise Exception("Not implemented")

class TimeStep:
    elapsed: float
    dt: float

    def __init__(self):
        self.elapsed = 0
        self.dt = 0

    def update(self, dt):
        self.elapsed += dt
        self.dt = dt

class UpdateLoop:
    updateList: List[IUpdateable]
    fixedUpdateList: List[IFixedUpdateable]
    startTime: float
    lastTime: float
    lastTimeStep: TimeStep
    lastFixedTimeStep: TimeStep
    fixedUpdateRemainder: float
    targetTimeStep: float

    def __init__(self, targetTimeStep:float, fixedTimeStep:float):
        self.targetTimeStep = targetTimeStep
        self.lastFixedTimeStep = TimeStep()
        self.lastFixedTimeStep.dt = fixedTimeStep
        self.updateList = []
        self.fixedUpdateList = []
        self.startTime = self.lastTime = monotonic()
        self.lastTimeStep = TimeStep()
        self.fixedUpdateRemainder = 0

    def add(self, updateable:IUpdateable):
        self.updateList.append(updateable)

    def remove(self, updateable:IUpdateable):
        raise Exception("Not implemented")

    def addFixed(self, updateable:IFixedUpdateable):
        self.fixedUpdateList.append(updateable)

    def removeFixed(self, updateable:IFixedUpdateable):
        raise Exception("Not implemented")

    async def run(self):
        while True:
            start = monotonic()
            self.lastTimeStep.update(start - self.lastTime)
            self.lastTime = start

            # Do regular update
            for updateable in self.updateList:
                updateable.update(self.lastTimeStep)

            # Update fixed time steps
            fixedUpdateTotalDt = self.lastTimeStep.dt + self.fixedUpdateRemainder
            while fixedUpdateTotalDt >= self.lastFixedTimeStep.dt:
                fixedUpdateTotalDt -= self.lastFixedTimeStep.dt
                self._fixedUpdate()

            self.fixedUpdateRemainder = fixedUpdateTotalDt

            end = monotonic()
            loopTime = end - start
            sleepTime = self.targetTimeStep - loopTime

            # Sleep until target time step
            await sleep(sleepTime)

    def _fixedUpdate(self):
        self.lastFixedTimeStep.update(self.lastFixedTimeStep.dt)
        for updateable in self.fixedUpdateList:
            updateable.updateFixed(self.lastFixedTimeStep)