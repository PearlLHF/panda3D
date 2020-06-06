import maya.cmds as mc
import maya.mel as mm
    
# create Input Window
if mc.window('expWindow', exists=True):
    mc.deleteUI('expWindow')


widgets = {}

widgets["win"] = mc.window('expWindow', rtf=True, title='Make Fold Window')

widgets["CLO"] = mc.columnLayout()

widgets["subDiv"] = mc.intFieldGrp('subDiv', label='SubDivision (9,19,...,149)')

widgets["fName"] = mc.textFieldGrp(label='File Name')

widgets["btn"] = mc.button(label='Make Fold', command=Fold1)

mc.showWindow(widgets["win"])


def Fold1(*args):
    text = mc.textFieldGrp(widgets["fName"], q=True, text=True)
    mc.select(all=True)
    if mc.ls(sl=True) != []:
        mc.delete()  # clear all items from workspace

    # create plane with 10 x divisions, 15 y divisions
    myPlane = mc.polyPlane(sx=10, sy=15, w=15, h=20, name='myPlane')

    eFrame = mc.intFieldGrp(widgets["subDiv"], query=True, value1=True)
    print('subdivs = ' + bytes(eFrame) + ', and file name is ' + text + '')

    # mc.select(myPlane[0].f[0:eFrame], r=True)
    mm.eval('int $eFrame = `intFieldGrp -query -value1 subDiv`;')
    mm.eval('select -r myPlane.f[0:$eFrame];')

    mc.rotate(-33.987404, 0, 0, relative=True,
              pivot=(0, 0, 8.666667), os=True, fo=True)
    # -33 stuff is the degree of folding, can also use manipPivot to change pivot of folding
    

