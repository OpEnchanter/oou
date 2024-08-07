"""Import project dependencies"""

import pygame, json, sys, os
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
        print("button Clicked")
        globalSceneManager.addScene("newTab", newTabInit, newTabFrame)
    if engine.uiButton.checkHover((elem.position[0], elem.position[1], elem.sprite.get_width(), elem.sprite.get_height())):
        pygame.draw.rect(
            elem.sprite, 
            (
                settings["appStyle"]["ui"]["color"]["buttonHoveredColor"][0],
                settings["appStyle"]["ui"]["color"]["buttonHoveredColor"][1],
                settings["appStyle"]["ui"]["color"]["buttonHoveredColor"][2]
            ),
            (0,0,100,50),
            0,
            0,
            settings["appStyle"]["ui"]["transform"]["button"]["topLeftRadius"],
            settings["appStyle"]["ui"]["transform"]["button"]["topRightRadius"],
            settings["appStyle"]["ui"]["transform"]["button"]["bottomLeftRadius"],
            settings["appStyle"]["ui"]["transform"]["button"]["bottomRightRadius"]
        )
        elem.sprite = engine.renderUtils.drawTextOnSurface(
            elem.sprite, 
            "New File", 
            None, 
            20, 
            100, 
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
            (0,0,100,50),
            0,
            0,
            settings["appStyle"]["ui"]["transform"]["button"]["topLeftRadius"],
            settings["appStyle"]["ui"]["transform"]["button"]["topRightRadius"],
            settings["appStyle"]["ui"]["transform"]["button"]["bottomLeftRadius"],
            settings["appStyle"]["ui"]["transform"]["button"]["bottomRightRadius"]
        )
        elem.sprite = engine.renderUtils.drawTextOnSurface(
            elem.sprite, 
            "New File", 
            None, 
            20, 
            100, 
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
    buttonSprite = pygame.Surface((100, 50), pygame.SRCALPHA)
    pygame.draw.rect(
        buttonSprite, 
        (
            settings["appStyle"]["ui"]["color"]["buttonColor"][0],
            settings["appStyle"]["ui"]["color"]["buttonColor"][1],
            settings["appStyle"]["ui"]["color"]["buttonColor"][2]
        ),
        (0,0,100,50),
        0,
        0,
        settings["appStyle"]["ui"]["transform"]["button"]["topLeftRadius"],
        settings["appStyle"]["ui"]["transform"]["button"]["topRightRadius"],
        settings["appStyle"]["ui"]["transform"]["button"]["bottomLeftRadius"],
        settings["appStyle"]["ui"]["transform"]["button"]["bottomRightRadius"]
    )
    

    buttonSprite = engine.renderUtils.drawTextOnSurface(
        buttonSprite, 
        "New File", 
        None, 
        20, 
        100, 
        (
            settings["appStyle"]["ui"]["color"]["fontColor"][0],
            settings["appStyle"]["ui"]["color"]["fontColor"][1],
            settings["appStyle"]["ui"]["color"]["fontColor"][2]
        )
    )
    
    scene.sceneUiManager.addElement(None, newFileButtonFrame, buttonSprite, (20, 55))

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