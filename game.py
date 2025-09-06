import pyengine
from time import sleep
print("test")

pyengine.add_object("spieler", "bilder/biene.png", None, 100, 100)
print(pyengine.running)
pyengine.run()
pyengine.objects[0]["y"] - 100
