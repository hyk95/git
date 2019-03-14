import numpy as np


class Road():
    def __init__(self, id, length, maxSpeed, numRoad, startId, endId, isTowWay):
        self.id = id
        self.length = length
        self.maxSpeed = maxSpeed
        self.numRoad = numRoad
        self.startId = startId
        self.endId = endId
        self.isTowWay = isTowWay
        self.roadVector = self.createRoadVector()

    def createRoadVector(self):
        if self.isTowWay == 1:
            roadVector = np.zeros([self.length, self.numRoad*2])
        else:
            roadVector = np.zeros([self.length, self.numRoad])
        return roadVector

