import os

def maya2egg(fileName, mayaVersion = '2019'):
    cmd = "maya2egg" + mayaVersion + " -a model -o " + fileName + ".egg " + fileName + ".mb"
    os.system(cmd)
