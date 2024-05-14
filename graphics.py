from tkinter import Tk, BOTH, Canvas

# WINDOW CLASS

# WINDOW CLASS'S CONSTRUCTOR

# The constructor should take a width and height.
# This will be the size of the new window we create in pixels.
# It should create a new root widget using Tk() and save it as a data member
# Set the title property of the root widget
# Create a Canvas widget and save it as a data member.
# Pack the canvas widget so that it's ready to be drawn
# Create a data member to represent that the window is "running", and set it to False

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False


    # REDRAW() METHOD
    # this method should call the root widget's update_idletasks() and update() methods
    # This will force the window to redraw itself

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
        

    # WAIT_FOR_CLOSE() METHOD
    # set the data memeber we created to track the "running" state of the window to True
    # call the self.redraw() method over and over as long as the running state remains True.

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("window closed...")


    # We need a draw_line method on our Window class.
    # It should take an instance of a Line and a fill_color as inputs,
    #  then call the Line's draw() method. 

    # DRAW_LINE() METHOD
    def draw_line(self, line, fill_color="black"):
        line.draw(self.__canvas, fill_color)


    # CLOSE() METHOD
    # set the running state to False
    # add another line to the constructor to call the protocol method on the root widget
    # to connect your close method to the "delete window" action.

    def close(self):
        self.__running = False


# POINT CLASS
# It should simply store 2 public data members, x and y
# which represent the x and y coordinates of the point.

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        

# LINE CLASS
# It should take 2 points as input, and save them as data members.
 
class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

# DRAW() METHOD
# The Line class need a draw() method that takes a canvas and a "fill color" as input.
# The "fill_color" will just be a string like " black" or "red".
# Next it should call the canvas's create_line() method.

    def draw(self, canvas, fill_color="black"):
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2)    




    

    