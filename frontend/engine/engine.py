import pygame, json, sys

class scene(object):
    def __init__(self, sceneBootScript, sceneFrameScript) -> None:
        self.data = {
            "bootScript": sceneBootScript,
            "frameScript": sceneFrameScript
        }

class sceneManager(object):
    def __init__(self):
        self.scenes = {}
        self.currentScene = "none"
    def addScene(self, sceneName, sceneBootScript, sceneFrameScript):
        self.currentScene = sceneName
        self.scenes[sceneName] = scene(sceneBootScript, sceneFrameScript) # Add scene to registry
        self.scenes[sceneName].data["bootScript"](self.scenes[self.currentScene]) # Run scene boot / init script
    def setScene(self, sceneName) -> bool:
        if sceneName in self.scenes.keys:
            self.currentScene = sceneName
            return True
        return False
    def removeScene(self, sceneName):
        self.scenes.pop(sceneName)
    def executeFrame(self):
        if self.currentScene in self.scenes.keys():
            self.scenes[self.currentScene].data["frameScript"](self.scenes[self.currentScene])

class uiElement(object):
    def __init__(self, elementBootScript, elementFrameScript, sprite, position):
        self.sprite = sprite
        self.bootScript = elementBootScript
        self.frameScript = elementFrameScript
        self.position = position

        elementBootScript(self)

class uiManager(object):
    def __init__(self, screen):
        self.elements = []
        self.screen = screen
    def addElement(self, elementBootScript, elementFrameScript, sprite, position):
        self.elements.append(uiElement(elementBootScript, elementFrameScript, sprite, position))
    def removeElement(self, index):
        self.elements.pop(index)
    def executeFrame(self):
        for elem in self.elements:
            elem.frameScript(elem)
            self.screen.blit(elem.sprite, elem.position)
            