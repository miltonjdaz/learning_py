# cannon ball program 
from math import sin, cos, radians 

def main():
    angle = float(input("Enter the launch angle (in degrees): "))
    vel = float(input("Enter the initial velocity (in meters/sec): "))
    hO = float(input("Enter the initial height (in meters): "))
    time = float(input("Enter the time interval between position calculations: "))
    
    # convert angle to radians 
    theta = radians(angle)

    # set the initial position and velocities in x & y directions 
    xpos = 0
    ypos = hO
    xvel = vel * cos(theta)
    yvel = vel * sin(theta)

    # loop until the ball hits the ground 
    while ypos >= 0.0:
        # calculate position and velovity in time seconds 
        xpos = xpos + time * xvel 
        yvel1 = yvel - time * 9.8 
        ypos = ypos + time * (yvel + yvel1)/2.0
        yvel = yvel1

    print("\nDistance traveled: {0:0.1f} meters.".format(xpos))

# updated version

from math import sin, cos, radians

class Projectile: 
    def __init__(self, angle, velocity, height):
        self.xpos = 0.0
        self.ypos = height
        theta = radians(angle)
        self.xvel = velocity * cos(theta)
        self.yvel = velocity * sin(theta)

    def update(self, time): 
        self.xpos = self.xpos + time * self.xvel 
        yvel1 = self.yvel - 9.8 * time 
        self.ypos = self.ypos + time * (self.yvel + yvel1)/2.0
        self.yvel = yvel1
    
    def getY(self):
        return self.ypos

    def getX(self):
        return self.xpos 

def getInputs():
    a = float(input("Enter the launch angle (in degrees): "))
    v = float(input("Enter the initial velocity (in meters/sec): "))
    h = float(input("Enter the initial height (in meters): "))
    t = float(input("Enter the time interval between position calculations: "))
    return a, v, h, t

def main():
    angle, vel, hO, time = getInputs()
    cball = Projectile(angle, vel hO)
    while cball.getY() >= 0:
        cball.update(time)
    print("\nDistance traveled: {0:0.1f} meters.".format(cball.getX()))