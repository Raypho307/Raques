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
           "y": y
           }
    objects.append(obj)
add_object("spieler", "bilder/biene.png", 100, 100)
"pygame"
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("purple")
    for obj in objects:
        screen.blit(obj["sprite"], (obj["x"], obj["y"]))
    pygame.display.flip()
    
pygame.quit()
