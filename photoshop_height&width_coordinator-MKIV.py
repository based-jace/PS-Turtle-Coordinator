again = ("yes")
MAX_WIDTH = 800 #Change these to reflect your Photoshop canvas size
MAX_HEIGHT = 480

halfW = (MAX_WIDTH / 2) * -1
halfH = MAX_HEIGHT / 2

while again != ("no"):

    widthCoord = []
    heightCoord = []    
        
    shapeName = raw_input("What's the name of this shape? ")
    shapePen = raw_input("What color is the outline of this shape? ")
    shapeFill = raw_input("What color fills in this shape? ")
    while True:
        try:
            points = input("How many points are there? ")
            break
        except:
            ValueError
            print("Please type a number.")
    
    print("")#adds a space for easier readability
        
    for vector in range(0, points):
        while True:
            try:
                oldWidth = input("What is the Photoshop X Coordinate for point %i? " %(vector+1))
                while (oldWidth < 0) or (oldWidth > MAX_WIDTH):
                    oldWidth = input("Please enter a number greater than -1 and less than %i: " % (MAX_WIDTH + 1))
                break
            except:
                ValueError
                print("Please enter a number.")
        newWidth = halfW + oldWidth
        widthCoord.append(newWidth)

        while True:
            try:
                oldHeight = input("What is the Photoshop Y Coordinate for point %i? " %(vector+1))
                while (oldHeight < 0) or (oldHeight > MAX_HEIGHT):
                    oldHeight = input("Please enter a number greater than -1 and less than %i: " % (MAX_HEIGHT + 1))
                break
            except:
                ValueError
                print("Please enter a number")
        newHeight = halfH - oldHeight
        heightCoord.append(newHeight)
        print("")#space

    print("")
    print("Your new coordinates are:") #This creates the entire geometric shape. Just copy and paste its output into your Turtle program.
    print("")
    print("#" + shapeName)
    print("pencolor('" + shapePen + "')")
    print("fillcolor('" + shapeFill + "')")
    print("goto(%i,%i)" %(widthCoord[0], heightCoord[0]))
    print("pendown()")
    print("begin_fill()")
    for allCoord in range(1, points):
        print("goto(%i,%i)" % (widthCoord[allCoord], heightCoord[allCoord]))
    print("goto(%i,%i)" %(widthCoord[0], heightCoord[0]))
    print("end_fill()")
    print("penup()")
    print("")
    
    again = raw_input("Is there another shape? ")
