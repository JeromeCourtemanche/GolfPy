import time
import math

class Sim:
    def __init__(self, ball, hole, angle, speed, spin, canvas):#eventually add l/r spin
        self.ball = ball
        self.hole = hole
        self.angle = angle
        self.speed = speed
        self.spin = spin

    def startSim(self):
        moving = True
        lastSimTime = time.time()
        timeDelta = 0

        while(moving):
            timeDelta = time.time() - lastSimTime
            speedX = self.speed*math.cos(self.angle)
            speedY = self.speed*math.sin(self.angle)
            self.ball.x += timeDelta*speedX
            self.ball.y += timeDelta*speedY + 0.5*9.8*(timeDelta**2)
               #slowdowns and deviations should be taken into account here :)

            if self.ball.y < self.hole.floor:
               moving = False

              #Here send message to redraw ball on canvas

        

