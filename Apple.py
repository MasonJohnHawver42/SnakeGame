import numpy as np
import cv2


class Apple:
    def __init__(self, pos):
        self.pos = pos

    def toImg(self):
        return cv2.imread("Apple.jpg")

    @staticmethod
    def makeRndApple(domain, range):
        return Apple(np.array([np.random.randint(domain), np.random.randint(range)]))


