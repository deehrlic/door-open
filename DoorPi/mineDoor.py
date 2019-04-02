import mcpi.minecraft as minecraft
import mcpi.block as block
import os

mc = minecraft.Minecraft.create()


while True:
        p = mc.player.getPos()
        #replace these values with whatever coordinate you want to be the trigger location for the motor
        if p.x > -5.7 and p.x < 5.3 and p.y == 0 and p.z > 12.2 and p.z < 12.7:
                os.system('python mineMotor.py')
                break
