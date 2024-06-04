import pygame
import math
from nodesystem import Node

class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[Node(x, y) for y in range(height)] for x in range(width)]

    def set_active(self, x, y, active):
        self.grid[x][y].active = active

    def set_start(self, x, y, start):
        self.grid[x][y].start = start
        self.grid[x][y].identifier = "START"

    def set_end(self, x, y, end):
        self.grid[x][y].end = end
        self.grid[x][y].identifier = "END"

    def set_corner(self, x, y, corner, id):
        self.grid[x][y].corner = corner
        self.grid[x][y].set_name(id)

    def draw(self, screen):
        for x in range(self.width):
            for y in range(self.height):
                node = self.grid[x][y]
                #color = (255, 55, 55) if node.active else (55, 55, 55)
                if node.start:
                    color = (125, 64, 165)
                elif node.corner:
                    color = (65, 165, 34)
                elif node.active:
                    color = (255, 55, 55)
                elif node.end:
                    color = (111, 23, 75)
                else:
                    color = (210, 210, 210)
                pygame.draw.rect(screen, color, (x * 10, y * 10, 10, 10))


