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
        self.scenes[sceneName] = scene(sceneBootScript, sceneFrameScript) # Add scene to registry
        self.scenes[sceneName].data["bootScript"]() # Run scene boot / init script
    def setScene(self, sceneName) -> bool:
        if sceneName in self.scenes.keys:
            self.currentScene = sceneName
            return True
        return False
    def removeScene(self, sceneName):
        self.scenes.pop(sceneName)
    def executeFrame(self):
        if self.currentScene in self.scenes.keys:
            self.scenes[self.currentScene].data["frameScript"]()