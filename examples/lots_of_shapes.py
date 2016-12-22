"""
An example of a simulation using lots of shapes.  The screencast developing this code can be found
here:
"""

from pyphysicssandbox import *
import random

width = 300
height = 300
how_many = 2000

window('Lots of Shapes!', width, height)

arm1 = box((100, 145), 100, 10, 100)
arm1.color = Color("yellow")

pivot1 = pivot((150, 150))
pivot1.connect(arm1)

motor(arm1, 5)

floor = static_box((0, 290), 300, 10)

for i in range(how_many):
    ball1 = ball((random.randint(0, width), random.randint(0, height)), 5)
    ball1.color = Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    ball1.wrap = True


run ()


