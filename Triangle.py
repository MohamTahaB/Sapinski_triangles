from math import *
import random
import matplotlib.pyplot as plt


class Triangle:
    def __init__(self, l):
        self.length = l
        self.trianglePoints = [[-l / 2, -l * sqrt(3) / 4], [0, l * sqrt(3) / 4], [l / 2, -l * sqrt(3) / 4]]
        self.points = []
        self.lastPoint = [l / 4, 0]
        self.points.append(self.lastPoint)

    def addPoint(self):
        n = random.randint(0, 2)
        auxPoint = self.trianglePoints[n]
        self.lastPoint = [(self.lastPoint[0] + auxPoint[0]) / 2, (self.lastPoint[1] + auxPoint[1]) / 2]
        self.points.append(self.lastPoint)

    def trace(self):
        for tp in self.trianglePoints:
            x, y = [tp[0]], [tp[1]]
            plt.plot(x, y, marker="o", markersize=2, markeredgecolor="green", markerfacecolor="green")
        for pt in self.points:
            x, y = [pt[0]], [pt[1]]
            plt.plot(x, y, marker="o", markersize=2, markeredgecolor="red", markerfacecolor="red")
        plt.show()
