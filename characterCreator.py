from graphics import*
from Button import*



def main():
    #win short for window
    win = GraphWin("character creator", 800, 600)
    #how to draw cricle in program
    C = Circle(Point(300, 300), 100)
    #^number are coordinates to make circle
    C.draw(win)

    R = Rectangle(Point(200, 500), Point(400, 575))
    R.draw(win)

    L = Line(Point(0, 0), Point(800, 600))
    L.draw(win)
    #line to cut window in half

    B = Button(win, Point(600, 100), Point(700, 175), "tomato", "Click me")
    #what to include in paranthesis is in Button.py file, ex) pt 1 and pt 2 + color and text


    
if __name__ == "__main__":
    main()
