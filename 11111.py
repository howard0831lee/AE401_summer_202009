# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 11:23:45 2020

@author: howar
"""

from mcpi.minecraft import Minecraft 
mc = Minecraft.create()
while True:
    x,y,z = mc.player.getTilePos()
    mc.postToChat(
            "You are located on x:"+
            str(x) +
            ", Y:" +
            str(y) +
            ", Z:" +
            str(z))