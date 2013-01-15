from vex import Vex
from pystroke.vector2 import Vector2
import pygame

class DemoCollectable(Vex):
    
    def __init__(self, x, y, score):
        Vex.__init__(self, x, y, pygame.Color(0, 255, 0), 
                     [Vector2(10, 0), Vector2(0, 10), Vector2(-10, 0),
                      Vector2(0, -10), Vector2(10, 0)], 
                      2)
        self.score = score