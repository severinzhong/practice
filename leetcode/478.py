# 478. Generate Random Point in a Circle
import random
class Solution:

    def __init__(self, radius, x_center, y_center):
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center
    def randPoint(self) :
        if self.radius == 0 :
            return
        while True :
            xx = self.x_center+(random.random()-0.5)*2*self.radius
            yy = self.y_center+(random.random()-0.5)*2*self.radius
            if (xx - self.x_center)**2 +(yy - self.y_center)**2 <= self.radius**2 :
                return [xx,yy]
if __name__ == '__main__' :
    obj = Solution(1,2,0)
    print(obj.randPoint())