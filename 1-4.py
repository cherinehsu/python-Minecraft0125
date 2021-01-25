from mcpi.minecraft import Minecraft
import time
cherinehsu = Minecraft.create()

X = 100
Y = 100
Z = 100

cherinehsu.player.setTilePos(X,Y,Z)
time.sleep(2)

X = X-50
Y = Y-50

cherinehsu.player.setTilePos(X,Y,Z)
time.sleep(2)

X = X-50
Y = Y-50

cherinehsu.player.setTilePos(X,Y,Z)