# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 11:46:11 2020

@author: Amit
"""

import turtle as trtl
rocketship_image = "rocketship.gif"

up = -50

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(rocketship_image)
#wn.bgpic("Screenshot 2020-11-18 at 8.47.14 PM.png")

rocketship = trtl.Turtle()

def start_pos():
  rocketship.pu()
  rocketship.goto(0,-250)

  rocketship.right(90)
start_pos()

def draw_rocketship(active_rocketship):
    active_rocketship.pu()
    active_rocketship.shape(rocketship_image)

def drop_rocketship():
  global up
  rocketship.pu()
  rocketship.clear()
  rocketship.forward(up)
  draw_rocketship(rocketship)


draw_rocketship(rocketship)

if wn.onkeypress(drop_rocketship, "3"):
  drop_rocketship()
