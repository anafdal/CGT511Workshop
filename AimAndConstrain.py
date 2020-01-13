#aimatfirst.py

import maya.cmds as cmds

selectionList=cmds.ls(orderedSelection=True)#pick object/order matters

if len(selectionList)>=2:
    #need to select 2 or more objects to constrain
    #print 'Selected items: %s' %(selectionList)

    targetName=selectionList[0]
    selectionList.remove(targetName)
    
    for objectName in selectionList:
        print 'Constraining %s towards %s'%(objectName,targetName)
        cmds.orientConstraint(targetName,objectName)
        #orient/rotation constraint
        
    
    
else:'Please select two objects or more'
