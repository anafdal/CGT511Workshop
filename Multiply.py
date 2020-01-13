#randominstances.py

import maya.cmds as cmds#import commands
import random

result=cmds.ls( orderedSelection=True)#for selected object

transformName=result[0]
instanceOrbits=cmds.group(empty=True, name=transformName+'_satellite_grp#')

for i in range(0,100):
    instanceSatellite=cmds.instance(transformName,name=transformName+'_satellite#') 

    x=random.randint(-10,10)
    z=random.randint(-10,10)
    y=random.randint(-10,10)
    
    cmds.move(x,y,z,instanceSatellite)#move the instances randomly

    scalingFactor=random.uniform(0.3,1.5)#scale randomly
    cmds.scale(scalingFactor,scalingFactor,scalingFactor,instanceSatellite)
   
   
    cmds.parent(instanceSatellite,instanceOrbits)#parent in group
   

cmds.xform(instanceOrbits,centerPivots=True)#pivot in center
