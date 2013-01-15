import pygame
from pygame.locals import *
from hud import *
import math
import random
from pystroke.locals import QUIT_FLAG, CONTINUE_FLAG, SWITCH_FLAG
from pystroke.game_engine import GameEngine
from pystroke.vector2 import Vector2
from pystroke.hud import HUDText

from demo_collectable import DemoCollectable
from demo_player import DemoPlayer


class DemoGameEngine(GameEngine):
    def __init__(self, screen, event_e):

        GameEngine.__init__(self, screen, event_e)
        self.player = DemoPlayer(400, 300)
        self.FPS = 60
        self.r_mod = int(self.FPS / 15)
        self.r_count = 0
        self.l_mod = int(self.FPS / 15)
        self.l_count = 0
        self.p_speed = int(self.FPS / 6)
        self.collectables = []
        self.score = 0
        self._hud.add(HUDText("score", pygame.Color(255, 255, 255), 
                              "score 0", (15, 25), 1, 2))
        
    def update(self):
        self.event_e.update()
        
        x_mod = 0
        y_mod = 0
        
        if self.get_key(K_a):
            x_mod -= self.p_speed
        if self.get_key(K_d):
            x_mod += self.p_speed
        if self.get_key(K_w):
            y_mod -= self.p_speed
        if self.get_key(K_s):
            y_mod += self.p_speed
            
        if self.get_key(K_LEFT):
            if self.l_count % self.l_mod == 0:
                self.player.rotate_by_radians(-math.pi/4)
            self.l_count += 1  
        elif self.get_key(K_RIGHT):
            if self.r_count % self.r_mod == 0:
                self.player.rotate_by_radians(math.pi/4)
            self.r_count += 1
        if self.get_key(K_UP):
            x_mod = self.player.rel_dir().x * self.p_speed
            y_mod = self.player.rel_dir().y * self.p_speed   
        elif self.get_key(K_DOWN):
            x_mod = -self.player.rel_dir().x * self.p_speed
            y_mod = -self.player.rel_dir().y * self.p_speed
        self.player.move(x_mod, y_mod, self.screen)  
        print self.player.rel_dir()
        
        if self.get_key(K_SPACE):
            self.spawn_collectables(10)
        
        collected = []
        
        for c in self.collectables:
            if c not in collected:     
                for p in c.points: 
                    if c not in collected:
                        if self.player.point_inside(Vector2(p.x+c.x, p.y+c.y)):
                            collected.append(c)
                        
            
        for c in collected:
            self.score += c.score
            self._hud.get("score").text = "score %d" % (self.score)
            self.collectables.remove(c)    
            print "Collected!"
        del collected
        
        if self.get_key(K_ESCAPE):
            print self.score
            return QUIT_FLAG
        self.clock.tick(self.FPS)
        return CONTINUE_FLAG
    
    def draw(self):

        self.draw_e.begin_draw(pygame.Color(0, 0, 0))
        self.draw_e.draw([self.player])
        self.draw_e.draw(self.collectables)
        self.draw_e.draw([self._hud])
        # Draw your drawables here
        # They must be passed in as lists
        # self.draw_e.draw([some_drawable, some_other_drawable])
        # self.draw_e.draw([another_drawable])
        self.draw_e.end_draw()
        
    def spawn_collectables(self, n):
        for i in xrange(0, n):
            x = random.randint(30, 770)
            y = random.randint(30, 570)
            self.collectables.append(DemoCollectable(x, y, 50))        