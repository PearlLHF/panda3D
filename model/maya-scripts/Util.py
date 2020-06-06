import maya.cmds as mc

def deleteAll():
    mc.select(all=True)
    if mc.ls(sl=True) != []:
        mc.delete()  # clear all items from workspace


def addPointLight(pos):
    pointLight = mc.pointLight(name='pointLight')
    mc.move(pos[0], pos[1], pos[2], pointLight)


# fileName need to include directory to the file, e.g.: "C:/Users/Pearl/Desktop/Fold.obj"
def exportObj(fileName):
    mc.file(fileName, force=True, options="groups=1;ptgroups=1;materials=1;smoothing=1;normals=1",
            type="OBJexport", pr=True, ea=True)