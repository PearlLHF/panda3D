import os


def maya2egg(fileName, mayaVersion='2019'):
    cmd = "maya2egg" + mayaVersion
    cmd += " -a model -o ./model/" + fileName + ".egg ./model/" + fileName + ".mb"
    os.system(cmd)

def convertAll(deleteOrigin = False, confirm = True):
    files = os.listdir('./model')
    print(files)

    for file in files:
        [fileName, extension] = file.split(".")
        if extension == 'mb':
            maya2egg(fileName)
    
            if confirm:
                deleteOrigin = (input("Delete Original " + fileName + ".mb file? (Y/N)") == "Y")
                
            if deleteOrigin:
                os.system("del /q model\\" + fileName + ".mb")

convertAll()
