import maya.cmds as mc
# from Util import *;

# degree: rotate degreee
# lightPos: the position of the point light
# fileName: str including the directory
def Fold1(degree=30, lightPos=(1, 10, -1), fileName='D:/OneDrive - HKUST Connect/20Spring_UROP/3D-Modeling/Texture/Fold1.obj'):
    deleteAll()

    # create plane with 10 x divisions, 15 y divisions
    myPlane = mc.polyPlane(sx=10, sy=15, w=15, h=20, name='myPlane')

    mc.select('myPlane.f[0:19]', r=True)

    mc.rotate(-degree, 0, 0, relative=True,
              pivot=(0, 0, 10), os=True, fo=True)

    addPointLight(lightPos)

    exportObj(fileName)


# degree: rotate degreee
# lightPos: the position of the point light
# fileName: str including the directory
def foldCorner(degree=30, lightPos=(1, 10, -1), fileName='D:/OneDrive - HKUST Connect/20Spring_UROP/3D-Modeling/Texture/foldCorner.obj'):
    mc.select(all=True)
    if mc.ls(sl=True) != []:
        mc.delete()  # clear all items from workspace

    myPlane = mc.polyPlane(sx=10, sy=15, w=15, h=20, name='myPlane')
    piv1 = mc.pointPosition('myPlane.vtx[24]')
    mc.move(0, 0, 0, myPlane)
    mc.rotate(0, -45, 0, myPlane, a=True,
              p=(piv1[0], piv1[1], piv1[2]), ws=True, fo=True)

    mc.select('myPlane.f[0:1]', 'myPlane.f[10:11]')
    mc.polyCut(cd='X', ch=1)
    piv2 = mc.pointPosition('myPlane.vtx[12]')

    mc.select('myPlane.f[0:1]', 'myPlane.f[10]')
    mc.rotate(0, 0, -degree, a=True,
              p=(piv2[0], piv2[1], piv2[2]), ws=True, fo=True)

    mc.rotate(0, 0, 0, myPlane, a=True,
              p=(piv1[0], piv1[1], piv1[2]), ws=True, fo=True)

    addPointLight(lightPos)

    exportObj(fileName)
