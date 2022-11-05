class TimeStep:
    elapsed: float
    dt: float

    def __init__(self):
        self.elapsed = 0
        self.dt = 0

    def update(self, dt):
        self.elapsed += dt
        self.dt = dt