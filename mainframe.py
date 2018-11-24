from importlib import reload
import network as n
import image2 as i
import mn as d


image = i.image(n, d)

def reloader():
    print("to reload network module:  \"n\" or \"network\"")
    print("to reload image module:    \"i\" or \"image\"")
    print("to reload all modules:     \"a\" or \"all\"" )
    print("to abort:                  \"abort\"")
    print("   ", end="")
    command = input("/sc$ ")

    if command == "network" or command == "n":
        for x in range(1):
            try:
                reload(n)
            except Exception as e:
                print("ERROR: reloading network module")
                print(e)
            print("   ", end="")
            print("network module reloaded")
    elif command == "image" or command == "i":
        for x in range(1):
            try:
                reload(i)
                image = i.image(n, d)
            except Exception as e:
                print("ERROR: reloading image modeule")
                print(e)
                break
            print("   ", end="")
            print("image module reloaded")
    elif command == "all" or command == "a":
        for x in range(1):
            try:
                reload(n)
            except Exception as e:
                print("ERROR: reloading network module")
                print(e)
                break
            print("   ", end="")
            print("network module reloaded")

            try:
                reload(i)
                image = i.image(n, d)
            except Exception as e:
                print("ERROR: reloading image modeule")
                print(e)
                break
            print("   ", end="")
            print("image module reloaded")
    elif command == "abort":
        pass
    else:
        print("   ", end="")
        print("invalid subcommand")
        reloader()
    return image

while True:
    command = input("/c$ ")
    if command == "exit" or command == "e":
        print("exiting")
        quit()
    elif command == "reload" or command == "r":
        image = reloader()
    elif command == "run":
        image.run()

