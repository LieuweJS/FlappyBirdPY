import pygame as pg
import time
import random
import math

canvasWidth = 400
canvasHeight = 400
pipes = []

class Player(object):
    x = canvasWidth/4
    y = canvasHeight/2
    size = 50
    gravity = 0.3
    lift = -7
    velocity = 0
    def updatePosition(self):
        self.velocity += self.gravity;
        self.y += self.velocity;
        if self.y > canvasHeight:
            self.y = canvasHeight
            self.velocity = 0
        if self.y < 0:
            self.y = 0;
            self.velocity = 0;
    def flap(self):
        self.velocity += self.lift

class Pipe(object):
    def __init__(self):
        self.pipeHeight =  math.floor(random.random() * 250)
        self.bottomHeight = self.pipeHeight + 150
        self.width = 20
        self.x = canvasWidth - self.width

def main():
    pg.init()
    canvas = pg.display.set_mode((canvasWidth, canvasHeight))
    y = canvasHeight/2
    totalFrames = 0
    player = Player()
    playerColor = (255,211,0)
    clock = pg.time.Clock()
    pipes.append(Pipe())
    while True:
        totalFrames += 1
        ev = pg.event.poll()
        if ev.type == pg.QUIT:
            break
        canvas.fill((0, 200, 255))
        pg.draw.ellipse(canvas, playerColor, (player.x, player.y, player.size, player.size))
        for pipe in pipes:
            if pipe.x <=0:
                del pipes[0]
            pg.draw.rect(canvas,(0,200,0),(pipe.x, 0, pipe.width, pipe.pipeHeight))
            pg.draw.rect(canvas,(0,200,0),(pipe.x, pipe.bottomHeight, pipe.width, canvasHeight - pipe.bottomHeight))
            pipe.x -= 1;
            if player.y > pipe.bottomHeight or player.y < pipe.pipeHeight:
                if player.x >= pipe.x and player.x <= (pipe.x + pipe.width):
                    pg.quit()
        if player.y <= 0 or player.y >= 400:
            pg.quit()
        pressed = pg.key.get_pressed()
        if totalFrames % 5 == 0:
          if pressed[pg.K_SPACE]:
              player.flap()
        player.updatePosition()
        if totalFrames % 120 == 0:
            pipes.append(Pipe())
        pg.display.flip()
        clock.tick(60)
    pg.quit()
main()
