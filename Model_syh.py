from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from panda3d.core import TextureStage, PointLight, DirectionalLight, AmbientLight, Spotlight

import imagesize
from math import sin,cos

class Model_syh(ShowBase):

    wid = 1.0
    hei = 1.0
    textureName = "0.jpg"
    modelName = "Paper.egg"
    screenshotName = ""

    def __init__(self, modelName="Paper.egg", textureName="0.jpg", screenshotName=""):
        ShowBase.__init__(self)
        self.lightX = 0
        self.loadModel(modelName, textureName, screenshotName)
        self.addPointLight()
        self.taskMgr.add(self.move_light,"move-light")

    def loadModel(self, modelName="Paper.egg", textureName="0.jpg", screenshotName=""):
        self.modelName = modelName
        path_to_model = "model/" + self.modelName

        self.textureName = textureName
        path_to_img = "texture/" + textureName

        # Load the environment model.
        self.scene = self.loader.load_model(path_to_model)
        # Reparent the model to render.
        self.scene.reparentTo(self.render)
        self.light_model = self.loader.load_model('models/misc/sphere')
        self.light_model.setScale(10,10,10)
        self.light_model.reparentTo(self.render)
        # Apply texture
        self.applyTexture(path_to_img, screenshotName)
        
    def move_light(self,task):
        dt = globalClock.getDt()
        self.plnp.setPos(cos(self.lightX)*100,sin(self.lightX)*100, 100)
        self.lightX += 2*dt
        self.light_model.setPos(self.plnp.getPos())
        return task.cont

    def setScreenshotName(self, fileName):
        if fileName != "":
            self.screenshotName = "./screenshot/" + \
                self.modelName + "-screenshot-" + fileName + ".jpg"

    # different lightings

    def addPointLight(self, color=(1, 1, 1, 1), pos=(0, 0, 100)):
        plight = PointLight('plight')
        plight.setColor(color)
        self.plnp = self.render.attachNewNode(plight)
        self.plnp.setPos(pos)
        self.render.setLight(self.plnp)
        

    def addDirectionalLight(self, color=(0.2, 0.2, 0.2, 1), pos=(0, 0, 100), hpr=(0, 0, 0)):
        dlight = DirectionalLight('my dlight')
        dlight.setColor(color)
        dlnp = self.render.attachNewNode(dlight)
        dlnp.setPos(pos)
        dlnp.setHpr(hpr)
        self.render.setLight(dlnp)

    def addAmbientLight(self, color=(0.2, 0.2, 0.2, 1), pos=(0, 0, 100)):
        alight = AmbientLight('alight')
        alight.setColor(color)
        alnp = self.render.attachNewNode(alight)
        alnp.setPos(pos)
        self.render.setLight(alnp)

    # camera task when applying texture(top view)
    def cameraTaskInit(self, task):
        self.camera.setPos(0, 0, (self.hei+self.wid)/self.wid*666)
        self.camera.setHpr(0, -90, 0)
        self.addPointLight(pos=(0, 0, (self.hei+self.wid)/self.wid*666))
        # self.addDirectionalLight(pos=(0, 0, (self.hei+self.wid)/self.wid*66))

        # take screenshot
        if self.screenshotName != "":
            self.screenshot(self.screenshotName, defaultFilename=False)

        return Task.cont

    # applying textures
    def applyTexture(self, path_to_img, screenshotName=""):
        self.wid, self.hei = imagesize.get(path_to_img)
        print(self.wid,self.hei)
        myTexture = self.loader.loadTexture(path_to_img)
        self.scene.setTexture(myTexture, 1)

        # Apply scale and position transforms on the model.
        self.scene.setScale(1, self.hei/self.wid, 1)
        self.scene.setPos(0, 0, 0)

        self.setScreenshotName(screenshotName)
        #self.taskMgr.add(self.cameraTaskInit, "cameraTaskInit")
