from math import *
from graphics import *
from wheel import *
class Car():
    def _init_(self,wheel_center,wheel_radius,center,radius,car_height):
        body_p1 = point(min(wheel_center.getx(),wheel2_center.gety(-car_height)))
        body_p2 = point(min(wheel_center.getx(),wheel2_center.gety(-car_height)))
        self.body = tesla(body_p1,body_p2)
        self.wheel1 = wheel(wheel1 center,0.1*wheel1_radius,wheel1_radius)
        self.wheel2 = wheel(wheel2 center,0.1*wheel2_radius,wheel1_radius)
        self.wheel3 = wheel(wheel3 center,0.1*wheel3_radius,wheel1_radius)
        self.wheel4 = wheel(wheel4 center,0.1*wheel4_radius,wheel1_radius)
    def animate(self,wheel,dxdx,dy,n):
        if n >0:
            self.move(dx,dy)
            win.after(100,self.animate)
