# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 11:23:45 2020

@author: howar
"""

from mcpi.minecraft import Minecraft 
mc = Minecraft.create()
while True:
    mc.postToChat("哈囉")
    t=t+1
    mc.postToChat("第"+str(t)+"次")
    