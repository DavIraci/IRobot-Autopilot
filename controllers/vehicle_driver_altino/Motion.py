
from Constants import MAX_ANGLE, MAX_SPEED
from Devices import Actuators
from PathPlanner import U_TURN
from PathRunner import PathRunner
from Utils import logger


class Motion:

    def __init__(self, actuators, pathRunner):
        self.actuators = actuators
        self.pathRunner = pathRunner
        

        actuators.setSpeed(0.5)

    def update(self):
        self.updatePathRunner()

    def updatePathRunner(self):
        newSpeed = self.pathRunner.getSpeed()
        newAngle = self.pathRunner.getSteeringAngle()
        if newAngle != U_TURN:
            logger.log("ACTUAL ANGLE: " + str(newAngle))
            self.actuators.setAngle(newAngle * MAX_ANGLE)
            self.actuators.setSpeed(newSpeed * MAX_SPEED)