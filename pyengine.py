import pygame

"init pygame"
pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Pyengine")
running = True

"Variables"
objects = []

"Functions"
def add_object(name, sprite_path, x=0, y=0):
    sprite = pygame.image.load(sprite_path)
    obj = {"name": name,
           "sprite": sprite,
           "x": x,
           "y": y,
           "script": None
           }
    objects.append(obj)

def add_script(objnumber, scriptname):
    objects[objnumber]["script"] = script
 add_object("spieler", "bilder/biene.png", 100, 100)
print(objects)
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
    screen.fill("purple")
    for obj in objects:
        screen.blit(obj["sprite"], (obj["x"], obj["y"]))
    pygame.display.flip()
    
pygame.quit()
