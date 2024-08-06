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

"""Scene Scripts"""
def homeFrame(scene):
    win.fill((
        settings["appStyle"]["ui"]["color"]["backgroundColor"][0],
        settings["appStyle"]["ui"]["color"]["backgroundColor"][1],
        settings["appStyle"]["ui"]["color"]["backgroundColor"][2]
    ))

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
            win.get_size()[0],
            30
        )
    )

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
            300,
            550
        ),
        0,
        0,
        settings["appStyle"]["ui"]["transform"]["inset"]["topLeftRadius"],
        settings["appStyle"]["ui"]["transform"]["inset"]["topRightRadius"],
        settings["appStyle"]["ui"]["transform"]["inset"]["bottomLeftRadius"],
        settings["appStyle"]["ui"]["transform"]["inset"]["bottomRightRadius"]

    )

def homeInit(scene):
    pass

globalSceneManager = engine.sceneManager()

globalSceneManager.addScene("home", homeInit, homeFrame)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    win.fill((0, 255, 0))

    globalSceneManager.executeFrame()

    pygame.display.flip()