from graphics import*
from Buttons import*


def darken(img):
    x = img.getWidth()
    y = img.getHeight()

    for i in range(x):
        for j in range(y):
            pix = img.getPixel(i, j)
            red = pix[0]
            green = pix[1]
            blue = pix[2]
            red = red - 50
            green = green - 50
            blue = blue - 50
            if (red<0):
                red = 0
            if (green<0):
                green = 0
            if (blue<0):
                blue = 0
           

            #print([red, green, blue])
            c = color_rgb(red, green, blue)
            img.setPixel(i, j, c)

def lighten(img):
    x = img.getWidth()
    y = img.getHeight()

    for i in range(x):
        for j in range(y):
            pix = img.getPixel(i, j)
            red = pix[0]
            green = pix[1]
            blue = pix[2]
            red = red + 50
            green = green + 50
            blue = blue + 50
            if (red>255):
                red = 255
            if (green>255):
                green = 255
            if (blue>255):
                blue = 255
           

            #print([red, green, blue])
            c = color_rgb(red, green, blue)
            img.setPixel(i, j, c)



def grayscale(img):
    x = img.getWidth()
    y = img.getHeight()

    for i in range(x):
        for j in range(y):
            pix = img.getPixel(i, j)
            red = pix[0]
            green = pix[0]
            blue = pix[0]
                

            c = color_rgb(red, green, blue)
            img.setPixel(i, j, c)
            

            
            

            #contrast - any "light" pixel --> more light more or less preserving the color for it
            # - any "dark pixel --> more dark

            #blur() is just making image fuzzy and blurry and transition smoother

def contrast(img):
    x = img.getWidth()
    y = img.getHeight()

    for i in range(x):
        for j in range(y):
            pix = img.getPixel(i, j)
            red = pix[0]
            green = pix[1]
            blue = pix[2]

            if red >= 128:
                red += 20
            elif red <128:
                red -= 20
            if blue >= 128:
                blue += 20
            elif blue <128:
                blue -= 20
            if green >= 128:
                green += 20
            elif green <128:
                green -= 20

            if red > 255:
                red = 255
            if red < 0:
                red = 0
            if blue > 255:
                blue = 255
            if blue < 0:
                blue = 0
            if green > 255:
                green = 255
            if green < 0:
                green = 0

            c = color_rgb(int(red), int(green), int(blue))
            img.setPixel(i, j, c)
'''x = img.getWidth()
    y = img.getHeight()

    for i in range(x):
        for j in range(y):
            pix = img.getPixel(i, j)
            red = pix[0]
            green = pix[1]
            blue = pix[2]

            alpha = 1.5
            red = alpha*(red - 128) + 128
            blue = alpha*(blue - 128) + 128
            green = alpha*(green - 128) + 128
            #lightens and darkens at same time
            #as long as its greater than 1, it will increase contrast '''
                    

def main():

    win = GraphWin("Image Example", 800, 600)
    win.setBackground('cyan')

    I = Image(Point(300, 300), "shrek.png")
    I.draw(win)

    B = Button(win, Point(600, 100), Point(700, 175), "tomato", "Darken")
    B2 = Button(win, Point(600, 200), Point(700, 275), "tomato", "Lighten")
    
    Q = Button(win, Point(600, 300), Point(700, 375), "misty rose", "QUIT")
    B3 = Button(win, Point(600, 400), Point(700, 475), "tomato", "GrayScale")
    B4 = Button(win, Point(600, 500), Point(700, 575), "tomato", "Contrast")
    while True:
        m = win.getMouse()
        
        if B.isClicked(m):
            darken(I)
            

        if B2.isClicked(m):
            lighten(I)

        if B3.isClicked(m):
            grayscale(I)

        if B4.isClicked(m):
            contrast(I)

        if Q.isClicked(m):
            break

    win.close()

if __name__ == "__main__":
    main()
    
