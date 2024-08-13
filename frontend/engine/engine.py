import pygame, json, sys

prevFrameMouseDown = [False, False, False]

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

        if elementBootScript != None:
            elementBootScript(self)

class uiManager(object):
    def __init__(self):
        self.elements = []
    def addElement(self, elementBootScript, elementFrameScript, sprite, position):
        self.elements.append(uiElement(elementBootScript, elementFrameScript, sprite, position))
    def removeElement(self, index):
        self.elements.pop(index)
    def executeFrame(self, screen):
        for elem in self.elements:
            elem.frameScript(elem)
            screen.blit(elem.sprite, elem.position)

class uiButton():
    def checkHover(boundingBox = pygame.rect):
        mx, my = pygame.mouse.get_pos()

        if (mx > boundingBox[0] and mx < boundingBox[0] + boundingBox[2] and 
            my > boundingBox[1] and my < boundingBox[1] + boundingBox[3]):
            return True
        return False
    def checkClick(boundingBox = pygame.rect, mouseButton = int):
        if (uiButton.checkHover(boundingBox) and
            pygame.mouse.get_pressed()[mouseButton] and
            not prevFrameMouseDown[mouseButton]):
                prevFrameMouseDown[mouseButton] = True
                return True

        prevFrameMouseDown[mouseButton] = False
        return False
    
class uiTextField():
    def computeInput(currentText):

        key_strings = [
            "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
            "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
            "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "=", "[", "]", "\\", ";", "'", ",", ".", "/", "`", "~",
            " "
        ]

        finalText = currentText

        keys = pygame.key.get_pressed()

        for key in keys:
            if pygame.key.name(key) in key_strings:
                finalText += pygame.key.name

        return finalText

    
class renderUtils():
    def drawTextOnSurface(surface = pygame.surface, text = str, fontName = str, fontSize = int, wrapLength = int, fontColor = tuple) -> pygame.surface:
        finalSurface = surface
        
        font = pygame.font.Font(None, fontSize)
        fontImage = font.render(text, True, fontColor, wraplength=wrapLength)

        finalSurface.blit(fontImage, (finalSurface.get_width()/2-fontImage.get_width()/2, finalSurface.get_height()/2-fontImage.get_height()/2))

        return finalSurface