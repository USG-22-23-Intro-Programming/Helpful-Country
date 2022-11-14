from graphics import*
from Button import*


def main():

    win = GraphWin("character creator", 800, 600)
    win.setBackground("violet")

    C = Circle(Point(300, 300), 150)
    C.draw(win)

    #R = Rectangle(Point(200, 500), Point(400, 575))
    #R.draw(win)

    #L = Line(Point(0, 0), Point(800, 600))
    #L.draw(win)

    BigEye1 = Circle(Point(200, 250), 50)
    BigEye2 = Circle(Point(400, 250), 50)

    smallEye1 = Circle(Point(250, 250), 20)
    smallEye2 = Circle(Point(350, 250), 20)

    BigNose = Polygon([Point(300, 250), Point(250, 350), Point(350, 350)])
    smallNose = Polygon([Point(300, 250), Point(280, 300), Point(320, 300)])
    
    
                   

    B = Button(win, Point(600, 100), Point(700, 175), "tomato", "Big Eyes")
    B2 = Button(win, Point(600, 200), Point(700, 275), "tomato", "Small Eyes")

    B3 = Button(win, Point(600, 300), Point(700, 375), "tomato", "Big Nose")
    B4 = Button(win, Point(600, 400), Point(700, 475), "tomato", "Small Nose")

    Q = Button(win, Point(600, 500), Point(700, 575), "misty rose", "QUIT")

    while True:
        m = win.getMouse()
        
        if B.isClicked(m):
            BigEye1.undraw()
            BigEye2.undraw()
            smallEye1.undraw()
            smallEye2.undraw()
            
            #B.undraw()
            #B2.draw(win)
            
            BigEye1.draw(win)
            BigEye2.draw(win)

        if B2.isClicked(m):
            smallEye1.undraw()
            smallEye2.undraw()
            BigEye1.undraw()
            BigEye2.undraw()

            #B2.draw()
            #B.undraw()
            
            smallEye1.draw(win)
            smallEye2.draw(win)

        if B3.isClicked(m):
            BigNose.undraw()
            smallNose.undraw()
            
            BigNose.draw(win)

        if B4.isClicked(m):
            BigNose.undraw()
            smallNose.undraw()

            smallNose.draw(win)

        if Q.isClicked(m):
            break

    win.close()

if __name__ == "__main__":
    main()
