"""Import project dependencies"""

import pygame, json, sys, os
origionalPath = list(sys.path)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import engine.engine as engine
sys.path = origionalPath

settings = {}

with open("settings.json", "r") as settings_file:
    settings = json.load(settings_file)

pygame.init()

win = pygame.display.set_mode((settings["screen"]["width"], settings["screen"]["height"]))

globalSceneManager = engine.sceneManager()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    win.fill((255, 255, 255))


    pygame.display.flip()