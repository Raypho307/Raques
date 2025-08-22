import pygame
from pygamevideo import Video
from time import sleep


"init pygame"
pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Pyengine")
running = True
video = Video("video.mp4")
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
           "gravity": 0
           }
    objects.append(obj)
def move():
    if event.key == pygame.K_w:
        print("etst")
"run scripts"
def run_script(name):
    for obj in objects:
        if obj["name"] == name and obj["script"] is not None:
            obj["script"]()
def apply_phisics(objnumber, gravity):
    objects[objnumber]["gravity"] = gravity
def apply_collision(objnumber):
    objtoappend = objects[objnumber]
    objectswc.append(objtoappend)
    objects.pop(objnumber)
add_object("spieler", "bilder/biene.png", move, 100, 100)
add_object("spieler1", "bilder/biene.png", move, 500, 100)
apply_collision(1)
#apply_phisics(0, 1)

print(objects)
print(objectswc)
"pygame"
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                objects[0]["x"] -= 10
            if event.key == pygame.K_RIGHT:
                objects[0]["x"] += 10
            if event.key == pygame.K_UP:
                objects[0]["y"] -=  10
            if event.key == pygame.K_DOWN:
                objects[0]["y"] +=  10
            run_script("spieler")
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
            if obj["y"] == obj1["y"] and obj["x"] == obj1["x"]:
                #print("test")
                obj1["y"]
    pygame.display.flip()
    
    sleep(0.01)
pygame.quit()
