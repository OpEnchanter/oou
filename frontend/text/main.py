"""Import project dependencies"""

import tkinter.filedialog
import pygame, json, sys, os, tkinter
originalPath = list(sys.path)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import engine.engine as engine
sys.path = originalPath

"""Load Settings"""
settings = {}

with open(os.path.join(os.path.dirname(__file__), "settings.json"), "r") as settings_file:
    settings = json.load(settings_file)


"""Initialize Pygame For GUI"""

pygame.init()

win = pygame.display.set_mode((settings["screenConfig"]["width"], settings["screenConfig"]["height"]), pygame.RESIZABLE)

pygame.display.set_caption("OpenSource Office Utilities Text")

"""Functions and Classes"""

def newTabInit(scene):
    pass
def newTabFrame(scene):
    pass

def newFileButtonFrame(elem):
    if engine.uiButton.checkClick((elem.position[0], elem.position[1], elem.sprite.get_width(), elem.sprite.get_height()), 0):
        print("Creating new File")
        globalSceneManager.addScene("newTab", newTabInit, newTabFrame)
    if engine.uiButton.checkHover((elem.position[0], elem.position[1], elem.sprite.get_width(), elem.sprite.get_height())):
        pygame.draw.rect(
            elem.sprite, 
            (
                settings["appStyle"]["ui"]["color"]["buttonHoveredColor"][0],
                settings["appStyle"]["ui"]["color"]["buttonHoveredColor"][1],
                settings["appStyle"]["ui"]["color"]["buttonHoveredColor"][2]
            ),
            (0,0,elem.buttonScale[0], elem.buttonScale[1]),
            0,
            0,
            settings["appStyle"]["ui"]["transform"]["button"]["topLeftRadius"],
            settings["appStyle"]["ui"]["transform"]["button"]["topRightRadius"],
            settings["appStyle"]["ui"]["transform"]["button"]["bottomLeftRadius"],
            settings["appStyle"]["ui"]["transform"]["button"]["bottomRightRadius"]
        )
        elem.sprite = engine.renderUtils.drawTextOnSurface(
            elem.sprite, 
            elem.buttonText, 
            None, 
            elem.buttonFontSize, 
            elem.buttonScale[0], 
            (
                settings["appStyle"]["ui"]["color"]["fontColor"][0],
                settings["appStyle"]["ui"]["color"]["fontColor"][1],
                settings["appStyle"]["ui"]["color"]["fontColor"][2]
            )
        )
    else:
        pygame.draw.rect(
            elem.sprite, 
            (
                settings["appStyle"]["ui"]["color"]["buttonColor"][0],
                settings["appStyle"]["ui"]["color"]["buttonColor"][1],
                settings["appStyle"]["ui"]["color"]["buttonColor"][2]
            ),
            (0,0,elem.buttonScale[0], elem.buttonScale[1]),
            0,
            0,
            settings["appStyle"]["ui"]["transform"]["button"]["topLeftRadius"],
            settings["appStyle"]["ui"]["transform"]["button"]["topRightRadius"],
            settings["appStyle"]["ui"]["transform"]["button"]["bottomLeftRadius"],
            settings["appStyle"]["ui"]["transform"]["button"]["bottomRightRadius"]
        )
        elem.sprite = engine.renderUtils.drawTextOnSurface(
            elem.sprite, 
            elem.buttonText, 
            None, 
            elem.buttonFontSize, 
            elem.buttonScale[0], 
            (
                settings["appStyle"]["ui"]["color"]["fontColor"][0],
                settings["appStyle"]["ui"]["color"]["fontColor"][1],
                settings["appStyle"]["ui"]["color"]["fontColor"][2]
            )
        )   

def openFileButtonFrame(elem):
    if engine.uiButton.checkClick((elem.position[0], elem.position[1], elem.sprite.get_width(), elem.sprite.get_height()), 0):
        print("Opening File")
        fileName = tkinter.filedialog.askopenfilename()
    if engine.uiButton.checkHover((elem.position[0], elem.position[1], elem.sprite.get_width(), elem.sprite.get_height())):
        pygame.draw.rect(
            elem.sprite, 
            (
                settings["appStyle"]["ui"]["color"]["buttonHoveredColor"][0],
                settings["appStyle"]["ui"]["color"]["buttonHoveredColor"][1],
                settings["appStyle"]["ui"]["color"]["buttonHoveredColor"][2]
            ),
            (0,0,elem.buttonScale[0], elem.buttonScale[1]),
            0,
            0,
            settings["appStyle"]["ui"]["transform"]["button"]["topLeftRadius"],
            settings["appStyle"]["ui"]["transform"]["button"]["topRightRadius"],
            settings["appStyle"]["ui"]["transform"]["button"]["bottomLeftRadius"],
            settings["appStyle"]["ui"]["transform"]["button"]["bottomRightRadius"]
        )
        elem.sprite = engine.renderUtils.drawTextOnSurface(
            elem.sprite, 
            elem.buttonText, 
            None, 
            elem.buttonFontSize, 
            elem.buttonScale[0], 
            (
                settings["appStyle"]["ui"]["color"]["fontColor"][0],
                settings["appStyle"]["ui"]["color"]["fontColor"][1],
                settings["appStyle"]["ui"]["color"]["fontColor"][2]
            )
        )
    else:
        pygame.draw.rect(
            elem.sprite, 
            (
                settings["appStyle"]["ui"]["color"]["buttonColor"][0],
                settings["appStyle"]["ui"]["color"]["buttonColor"][1],
                settings["appStyle"]["ui"]["color"]["buttonColor"][2]
            ),
            (0,0,elem.buttonScale[0], elem.buttonScale[1]),
            0,
            0,
            settings["appStyle"]["ui"]["transform"]["button"]["topLeftRadius"],
            settings["appStyle"]["ui"]["transform"]["button"]["topRightRadius"],
            settings["appStyle"]["ui"]["transform"]["button"]["bottomLeftRadius"],
            settings["appStyle"]["ui"]["transform"]["button"]["bottomRightRadius"]
        )
        elem.sprite = engine.renderUtils.drawTextOnSurface(
            elem.sprite, 
            elem.buttonText, 
            None, 
            elem.buttonFontSize, 
            elem.buttonScale[0], 
            (
                settings["appStyle"]["ui"]["color"]["fontColor"][0],
                settings["appStyle"]["ui"]["color"]["fontColor"][1],
                settings["appStyle"]["ui"]["color"]["fontColor"][2]
            )
        )   


def homeFrame(scene):

    win.fill((
        settings["appStyle"]["ui"]["color"]["backgroundColor"][0],
        settings["appStyle"]["ui"]["color"]["backgroundColor"][1],
        settings["appStyle"]["ui"]["color"]["backgroundColor"][2]
    ))

    # Draw tabs bar
    pygame.draw.rect(
        win, 
        (
            settings["appStyle"]["ui"]["color"]["tabsBarColor"][0],
            settings["appStyle"]["ui"]["color"]["tabsBarColor"][1],
            settings["appStyle"]["ui"]["color"]["tabsBarColor"][2]
        ),
        (
            0, 
            0, 
            win.get_width(),
            30
        )
    )

    # Draw quick actions menu
    pygame.draw.rect(
        win, 
        (
            settings["appStyle"]["ui"]["color"]["insetColor"][0],
            settings["appStyle"]["ui"]["color"]["insetColor"][1],
            settings["appStyle"]["ui"]["color"]["insetColor"][2]
        ),
        (
            10, 
            45, 
            win.get_width()-20,
            550
        ),
        0,
        0,
        settings["appStyle"]["ui"]["transform"]["inset"]["topLeftRadius"],
        settings["appStyle"]["ui"]["transform"]["inset"]["topRightRadius"],
        settings["appStyle"]["ui"]["transform"]["inset"]["bottomLeftRadius"],
        settings["appStyle"]["ui"]["transform"]["inset"]["bottomRightRadius"]

    )

    # Draw UI Elements
    scene.sceneUiManager.executeFrame(win)

def homeInit(scene):
    scene.sceneUiManager = engine.uiManager()
    buttonScale = (300, 40)
    buttonFontSize = 20
    newFileButtonText = "Create New File"
    buttonSprite = pygame.Surface(buttonScale, pygame.SRCALPHA)
    pygame.draw.rect(
        buttonSprite, 
        (
            settings["appStyle"]["ui"]["color"]["buttonColor"][0],
            settings["appStyle"]["ui"]["color"]["buttonColor"][1],
            settings["appStyle"]["ui"]["color"]["buttonColor"][2]
        ),
        (0,0,buttonScale[0], buttonScale[1]),
        0,
        0,
        settings["appStyle"]["ui"]["transform"]["button"]["topLeftRadius"],
        settings["appStyle"]["ui"]["transform"]["button"]["topRightRadius"],
        settings["appStyle"]["ui"]["transform"]["button"]["bottomLeftRadius"],
        settings["appStyle"]["ui"]["transform"]["button"]["bottomRightRadius"]
    )
    

    buttonSprite = engine.renderUtils.drawTextOnSurface(
        buttonSprite, 
        newFileButtonText, 
        None, 
        buttonFontSize, 
        buttonScale[0], 
        (
            settings["appStyle"]["ui"]["color"]["fontColor"][0],
            settings["appStyle"]["ui"]["color"]["fontColor"][1],
            settings["appStyle"]["ui"]["color"]["fontColor"][2]
        )
    )
    scene.sceneUiManager.addElement(None, newFileButtonFrame, buttonSprite, (20, 55))
    scene.sceneUiManager.elements[len(scene.sceneUiManager.elements)-1].buttonScale = buttonScale
    scene.sceneUiManager.elements[len(scene.sceneUiManager.elements)-1].buttonFontSize = buttonFontSize
    scene.sceneUiManager.elements[len(scene.sceneUiManager.elements)-1].buttonText = newFileButtonText

    openFileButtonText = "Open File"
    buttonSprite = pygame.Surface(buttonScale, pygame.SRCALPHA)
    pygame.draw.rect(
        buttonSprite, 
        (
            settings["appStyle"]["ui"]["color"]["buttonColor"][0],
            settings["appStyle"]["ui"]["color"]["buttonColor"][1],
            settings["appStyle"]["ui"]["color"]["buttonColor"][2]
        ),
        (0,0,buttonScale[0], buttonScale[1]),
        0,
        0,
        settings["appStyle"]["ui"]["transform"]["button"]["topLeftRadius"],
        settings["appStyle"]["ui"]["transform"]["button"]["topRightRadius"],
        settings["appStyle"]["ui"]["transform"]["button"]["bottomLeftRadius"],
        settings["appStyle"]["ui"]["transform"]["button"]["bottomRightRadius"]
    )
    

    buttonSprite = engine.renderUtils.drawTextOnSurface(
        buttonSprite, 
        openFileButtonText, 
        None, 
        buttonFontSize, 
        buttonScale[0], 
        (
            settings["appStyle"]["ui"]["color"]["fontColor"][0],
            settings["appStyle"]["ui"]["color"]["fontColor"][1],
            settings["appStyle"]["ui"]["color"]["fontColor"][2]
        )
    )
    scene.sceneUiManager.addElement(None, openFileButtonFrame, buttonSprite, (20, 105))
    scene.sceneUiManager.elements[len(scene.sceneUiManager.elements)-1].buttonScale = buttonScale
    scene.sceneUiManager.elements[len(scene.sceneUiManager.elements)-1].buttonFontSize = buttonFontSize
    scene.sceneUiManager.elements[len(scene.sceneUiManager.elements)-1].buttonText = openFileButtonText

globalSceneManager = engine.sceneManager()

globalSceneManager.addScene("home", homeInit, homeFrame)

while True:
    win.fill((0, 255, 0))

    globalSceneManager.executeFrame()

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()