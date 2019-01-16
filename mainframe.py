from importlib import reload
import network as n
import image2 as i
import mn_d as d


image = i.image(n, d)

while True:
    command = input("/c$ ")
    if command == "exit" or command == "e":
        print("exiting")
        quit()
    elif command == "reload" or command == "r":
        try:
            reload(n)
            reload(i)
            image = i.image(n, d)
        except Exception as e:
            print("ERROR: reloading modules")
            print(e)
    elif command == "run":
        image.run()

