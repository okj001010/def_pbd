# src/objects/Line.py

import numpy as np
import pyglet
from pyglet import shapes
from .Object import Object

class Line(Object):
    """
    init Plaane
        center: numpy array [x, y]
            center of the line
        normal: numpy array [x, y]
            normal of the line
        color: tuple(r, g, b), optional
            rgb color of the circle, range[0-1]
    """
    def __init__(self, center, normal=(0,1), L=1000, color=(1,1,1), drest=0.001):
        self.center = np.array(center, dtype=np.float32)
        normv = np.array(normal, dtype=np.float32)
        self.normal = normv / np.linalg.norm(normv)
        self.color = color
        self.drest = drest
        self.L = L

    """
    @OVERRIDE
    draws the object
        scene: pyglet.graphics.Batch
            the scene object
    """
    def draw(self, scene):
        scale = 300.0
        offset_x = 400.0
        offset_y = 300.0
        c255 = tuple(int(c*255) for c in self.color)

        # a very long line, passing "center", perpendicular to normal
        perp = np.array([self.normal[1], -self.normal[0]], dtype=np.float32)
        p1 = self.center + perp*(self.L*0.5)
        p2 = self.center - perp*(self.L*0.5)

        line_shape = shapes.Line(
            x=p1[0]*scale+offset_x,
            y=p1[1]*scale+offset_y,
            x2=p2[0]*scale+offset_x,
            y2=p2[1]*scale+offset_y,
            width=2,
            color=c255,
            batch=scene
        )

    """
    @OVERRIDE
    solves the collision constraint for a point p
        p: numpy array [x, y]
            the point which collides
    """
    def solve_collision_constraint(self, p, x):
        cp = p - self.center
        cpdrest = cp - self.drest * self.normal
        
        l = abs(np.dot(cpdrest, self.normal))
        if np.dot(cpdrest, self.normal) < 0:
            return l * self.normal
        else:
            return np.array([0.0, 0.0], dtype=np.float32)