from pystroke.vex import Vex
from pystroke.vector2 import Vector2
import pygame

class DemoPlayer(Vex):
    
    def __init__(self, x, y):
        Vex.__init__(self, x, y, pygame.Color(255, 0, 255), 
                     [Vector2(20, 30), Vector2(30, 0), Vector2(10, 10),
                      Vector2(0, -10), Vector2(-10, 10), Vector2(-30, 0),
                      Vector2(-20, 30), Vector2(-10, 20), Vector2(-4, 24),
                      Vector2(4, 24), Vector2(10, 20), Vector2(20, 30)], 
                      2, 1, 1)