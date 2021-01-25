from mcpi.minecraft import Minecraft
cherinehsu = Minecraft.create()
import time

i=0
while True:
    i = i+1
    cherinehsu.postToChat("第"+str(i)+"次")
    time.sleep(3)