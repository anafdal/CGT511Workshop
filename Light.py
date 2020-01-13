#lights.py

import maya.cmds as cmds
import random


lightGroup=cmds.group(empty=True,name='lightGroup')#create group

for i in range(0,50):
  result=cmds.pointLight(intensity=1.0,name='light_#',rgb=(random.randint(0,1)
, random.randint(0,1), random.randint(0,1)),position=(random.uniform(-10,10)
, random.uniform(-10,10), random.uniform(-10,10)) ,softShadow=0.5)#pointlight

  cmds.parent(result,lightGroup)