# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 11:23:45 2020

@author: howar
"""

from mcpi.minecraft import Minecraft 
mc = Minecraft.create()
x,y,z = mc.player.getTilePos()
mc.player.setTilePos(x,y,z)