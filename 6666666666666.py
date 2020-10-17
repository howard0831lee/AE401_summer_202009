from mcpi.minecraft import Minecraft
import time

mc = Minecraft.create()

time.sleep(5)

x,y,z=mc.player.getTilePos()

mc.setBlock(x,y,z,57)
time.sleep(1)
mc.setBlock(x,y+1,z,57)
time.sleep(1)
mc.setBlock(x,y+2,z,57)
time.sleep(1)
mc.setBlock(x,y+3,z,57)
time.sleep(1)
mc.setBlock(x,y+4,z,57)
time.sleep(1)
mc.setBlock(x,y+5,z,57)
time.leep(1)
mc.setBlock(x,y+6,z,57)
time.sleep(1)
mc.setBlock(x,y+7,z,57)