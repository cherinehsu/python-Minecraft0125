from mcpi.minecraft import Minecraft
cherinehsu = Minecraft.create()

cherinehsu.postToChat("I'm watching you")

while True:
    x,y,z = cherinehsu.player.getTilePos()
    cherinehsu.postToChat(" X:"+str(x)+" Y:"+str(y)+" Z:"+str(z))