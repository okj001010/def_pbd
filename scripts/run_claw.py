# scripts/run_claw.py

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from simulation.ClawSimulation import ClawSimulation
from defobjects.DefObject import DefObject
from objects.Line import Line
from objects.Square import Square
from objects.Circle import Circle
from objects.Claw import Claw

def main():
    sim = ClawSimulation("claw machine", dt=0.0005, iterations=5, selfCollision=True)
    
    claw = Claw(center=(-0.5, 0.0), size=(0.6, 0.2), color=(0, 0, 0))
    sim.add_claw(claw)
    
    # set doll
    # doll = DefObject(num=(5, 5), spacing=0.05, origin=(-0.5, -0.8), KS=1.0, KC=1.0)
    doll = DefObject(num=(5, 5), spacing=0.05, origin=(-0.5, -0.8), KS=0.5, KC=1.0)
    sim.set_def_object(doll)

    # add walls
    walls = []
    walls.append(Line(center=(0.0, -1.0), normal=(0,1), color=(1, 0, 0)))
    walls.append(Line(center=(-1.0, 0.0), normal=(1,0), color=(1, 0, 0)))
    walls.append(Line(center=(1.0, 0.0), normal=(-1,0), color=(1, 0, 0)))
    for wall in walls:
        sim.add_object(wall)
    
    # add squares (basket)
    squares = []
    squares.append(Square(center=(0.1, -0.7), size=(0.2, 0.6), color=(0, 0, 1)))
    squares.append(Square(center=(0.9, -0.7), size=(0.2, 0.6), color=(0, 0, 1)))
    for square in squares:
        sim.add_object(square)
        
    # add circles (gate)
    circles = []
    circles.append(Circle(center=(0.22, -0.4), radius=0.22, color=(0, 0, 1)))
    circles.append(Circle(center=(0.78, -0.4), radius=0.22, color=(0, 0, 1)))
    for circle in circles:
        sim.add_object(circle)
    
    # sim.set_wind((1.0, 0.0))
    
    sim.run()

if __name__ == "__main__":
    main()
