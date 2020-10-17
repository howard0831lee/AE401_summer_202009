from mcpi.minecraft import Minecraft
import time

mc = Minecraft.create()

time.sleep(5)

x,y,z=mc.player.getTilePos()

mc.setBlocks(
    x+100,y-1,z+100,
    x-100,y-1,z-100,57)
    