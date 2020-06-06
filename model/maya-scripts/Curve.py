import maya.cmds as mc
# from Util import *;


# lightPos: the position of the point light
# fileName: str including the directory
def bendHandle(curv=90, lowB=0, highB=0.5, ro=(60, 0, 90), pos=(-5, 0, 6), lightPos=(1, 10, -1), fileName='D:/OneDrive - HKUST Connect/20Spring_UROP/3D-Modeling/Texture/bendHandle.obj'):
    deleteAll()

    # create plane with 10 x divisions, 15 y divisions
    myPlane = mc.polyPlane(sx=10, sy=15, w=15, h=20, name='myPlane')

    bend = mc.nonLinear(myPlane, type='bend', curvature=curv,
                        lowBound=-lowB, highBound=highB)
    mc.rotate(ro[0], ro[1], ro[2], bend, a=True, ws=True, fo=True)
    mc.move(pos[0], pos[1], pos[2], bend)

    addPointLight(lightPos)
    exportObj(fileName)


def bookShape(curv1=90, lowB1=0.5, highB1=0.5, ro1=(90, 180, 90),
              curv2=90, lowB2=0.5, highB2=0.5, ro2=(-90, 180, 90),
              lightPos=(1, 10, -1), fileName='D:/OneDrive - HKUST Connect/20Spring_UROP/3D-Modeling/Texture/bookShaped.obj'):
    deleteAll()

    myPlane1 = mc.polyPlane(sx=20, sy=15, w=30, h=20, name='myPlane1')
    bend1 = mc.nonLinear(myPlane1, type='bend', curvature=curv1,
                        lowBound=-lowB1, highBound=highB1)
    mc.rotate(ro1[0], ro1[1], ro1[2], bend1, a=True, ws=True, fo=True)

    piv1 = mc.pointPosition('myPlane1.vtx[325]')
    mc.select(bend1, myPlane1)
    mc.move(0, 0, -piv1[2], r=True)

    myPlane2 = mc.polyPlane(sx=20, sy=15, w=30, h=20, name='myPlane2')
    bend2 = mc.nonLinear(myPlane2, type='bend', curvature=curv2,
                        lowBound=-lowB2, highBound=highB2)
    mc.rotate(ro2[0], ro2[1], ro2[2], bend2, a=True, ws=True, fo=True)

    piv2 = mc.pointPosition('myPlane2.vtx[10]')
    mc.select(bend2, myPlane2)
    mc.move(0, 0, -piv2[2], r=True)

    mc.polyUnite(myPlane1, myPlane2, ch=1, mergeUVSets=1, centerPivot=True, n='myPlane')

    addPointLight(lightPos)
    exportObj(fileName)

    
bookShape()
