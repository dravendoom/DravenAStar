import pygame
import math

class Node:
    def __init__(self, x, y, active=False, start=False, corner=False, end=False):
        self.x = x
        self.y = y
        self.active = active
        self.start = start
        self.corner = corner
        self.end = end
        self.neighbors = []
        self.identifier = ""
        self.distance = 0
        self.g = 0
        self.h = 0
        self.f = 0

    def __lt__(self, neighbor):
        return self.f < neighbor.f

    def set_neighbor(self, node):
        self.neighbors.append(node)

    def set_name(self, id):
        self.identifier = id
