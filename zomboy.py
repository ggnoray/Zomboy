from mine import Minecraft
mc = Minecraft()
import time
import random
import sys

def didPlayerDie(pos):
    return pos.x < 15 and pos.y < 15 and pos.z < 15

def didEntityDie(entity):
    try:
        mc.entity.getPos(entity)
        return False
    except:
        return True

def getBlockLookingAt():
    playerPos = mc.player.getPos()
    playerDir = mc.player.getDirection()
    blockat = 0
    rayTrace = playerPos
    while blockat == 0:
        rayTrace += playerDir
        blockat = mc.getBlock(rayTrace)
    return rayTrace

pos = mc.player.getPos()
entityZombie = "Zombie"
entitySkelotn = "Skeleton"
entityCreeper = "Creeper"
entities = [entityZombie, entitySkelotn, entityCreeper]
mobs = []
level = 1
playerdead = False

mc.setting("world_immutable", False)
mc.player.setPos(0, 78, -793)
while True:1
    spawnpos = getBlockLookingAt()
    print("Level " + str(level) + ". Here they come!")
    for i in range(level * 3):
        mob = mc.spawnEntity(random.choice(entities), spawnpos.x, spawnpos.y + 2, spawnpos.z)
        mobs.append(mob)
        time.sleep(1)
    levelEnded = False
    while levelEnded == False:
        playerdead = didPlayerDie(mc.player.getPos())
        if playerdead == True:
            print("Game over!")
            sys.exit(0)
            pass
        alldead = True
        for entity in mobs:
            dead = didEntityDie(entity)
            if dead == False:
                alldead = False
        if alldead == True:
            levelEnded = True
    print("Level Ended")
    print("You have 10 seconds to breathe SO BREATHE.")
    time.sleep(10)
    level += 1
