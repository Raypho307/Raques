import pygame
from pygamevideo import Video


"init pygame"
pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Pyengine")
running = True
video = Video("video.mp4")
video.play()

"Variables"
objects = []

"Functions"
def add_object(name, sprite_path, script, x=0, y=0):
    sprite = pygame.image.load(sprite_path)
    obj = {"name": name,
           "sprite": sprite,
           "x": x,
           "y": y,
           "script": script
           }
    objects.append(obj)
def move():
    if event.key == pygame.K_w:
        print("etst")
add_object("spieler", "bilder/biene.png", move, 100, 100)
print(objects)
"run scripts"
def run_script(name):
    for obj in objects:
        if obj["name"] == name and obj["script"] is not None:
            obj["script"]()
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
    video.draw_to(screen, (0, 0))
    pygame.display.flip()
    
    
pygame.quit()
