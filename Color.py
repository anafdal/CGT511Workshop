#color.py

import maya.cmds as cmds
import random

#cmds.pointLight(intensity=1.0,name='light_#',position=(0, 0, 0), rgb=(1,0,0))

result=cmds.ls( orderedSelection=True)



def assign_shader(shader, objects):
    # get the shadingGroup with listConnections
    shading_group = cmds.listConnections(shader, type='shadingEngine')[-1]
    # use `sets` to force the objects into the shading group
    cmds.sets(objects, fe=shading_group)
 
new_shader = cmds.shadingNode('lambert', asShader=True, name='result')
new_sg = cmds.sets(renderable=True, noSurfaceShader=True, empty=True)
cmds.connectAttr(new_shader + '.outColor', new_sg + ".surfaceShader", force=True)

cmds.setAttr('lambert1' + ".color", random.randint(0,1),random.randint(0,1),random.randint(0,1))
