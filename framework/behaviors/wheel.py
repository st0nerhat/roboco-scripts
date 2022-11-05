from controllables import DCMotor

class Wheel:
    motor: DCMotor
    radius: float

    def __init__(self, motor:DCMotor, radius:float):
        self.motor = motor
        self.radius = radius

    def stop(self):
        self.motor.stop()

    def spin(self, linearVelocity:float):
        print("spin")
        angularVelocity = linearVelocity / self.radius
        power = angularVelocity / self.motor.max_velocity
        self.motor.spin(power)