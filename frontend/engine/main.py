import pygame, json, sys

settings = {}

with open("settings.json", "r") as settings_file:
    settings = json.load(settings_file)

pygame.init()

win = pygame.display.set_mode((settings["screen"]["width"], settings["screen"]["height"]))

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

globalSceneManager = sceneManager()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    win.fill((255, 255, 255))


    pygame.display.flip()