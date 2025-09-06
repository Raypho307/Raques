import pygame
from pygamevideo import Video
from time import sleep
import importlib.util
import os

"init pygame"
pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Pyengine")
running = True
#video = Video("video.mp4")
#video.play()
"Variables"
objects = []
objectswc = []

"Functions"
def add_object(name, sprite_path, script, x=0, y=0):
    sprite = pygame.image.load(sprite_path)
    obj = {"name": name,
           "sprite": sprite,
           "x": x,
           "y": y,
           "script": script,
           "gravity": 0,
           "cry": 0,
           "crx": 0
           }
    objects.append(obj)
def apply_phisics(objnumber, gravity):
    objects[objnumber]["gravity"] = gravity
def apply_collision(objnumber):
    objects[objnumber]["cry"] = 80
    objects[objnumber]["crx"] = 60
    objtoappend = objects[objnumber]
    objectswc.append(objtoappend)
    objects.pop(objnumber)
def build_game():
    if importlib.util.find_spec("PyInstaller") is None:
        os.system("pip install pyinstaller")
    os.system(f"pyinstaller --onefile game.py")
#add_object("spieler", "bilder/biene.png", None, 100, 100)
#add_object("spieler1", "bilder/biene.png", move, 200, 100)
#apply_collision(1)
#apply_phisics(0, 1)
#build_game()

print(objects)
print(objectswc)
"pygame"
def run():
    global running
    while running:
        #print("test")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            for obj in objects:
                if obj["script"] != None:
                    obj["script"]()
        screen.fill("purple")
        for obj in objects:
            screen.blit(obj["sprite"], (obj["x"], obj["y"]))
        for obj in objectswc:
            screen.blit(obj["sprite"], (obj["x"], obj["y"]))
        #video.draw_to(screen, (0, 0))
        for obj in objects:
            obj["y"] += obj["gravity"]
        for obj in objectswc:
            for obj1 in objects:
                if obj["y"] - obj["cry"] == obj1["y"] and obj["x"] - obj1["x"] < obj["crx"] and obj["x"] - obj1["x"] > obj["crx"] - obj["crx"] *2:
                    obj1["y"] -= 10
                if obj["x"] - obj["crx"] == obj1["x"] and obj["y"] - obj1["y"] < obj["cry"] and obj["y"] - obj1["y"] > obj["cry"] - obj["cry"] *2:
                    obj1["x"] -= 10
                if obj["y"] + obj["cry"] == obj1["y"] and obj["x"] - obj1["x"] < obj["crx"] and obj["x"] - obj1["x"] > obj["crx"] - obj["crx"] *2:
                    obj1["y"] += 10
                if obj["x"] + obj["crx"] == obj1["x"] and obj["y"] - obj1["y"] < obj["cry"] and obj["y"] - obj1["y"] > obj["cry"] - obj["cry"] *2:
                    obj1["x"] += 10
        pygame.display.flip()
        sleep(0.01)
    pygame.quit()