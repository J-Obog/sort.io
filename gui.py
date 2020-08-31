from graphics import *

methods = ["Bubble Sort", "Insertion Sort", "Selection Sort"]

# Draw a single bar
def drawBar(window, x1, y1, x2, y2):
    bar = Rectangle(Point(x1, y1), Point(x2, y2)) 
    bar.setFill(color_rgb(255, 255, 255)) 
    bar.draw(window)


# Initially load all bars
def renderBars(window, array):
    W = window.getWidth()
    H = window.getHeight()
    mv = max(array)    
    w = (W/len(array))-5
    for [i,v] in enumerate(array): 
        x1 = i*w
        x2 = x1+w
        y1 = 0 
        y2 = (H*(v/mv))-10
        drawBar(window, x1, y1, x2, y2)





def sortVisual(method, array):
    winName = methods[method]
    window = GraphWin(winName, 700, 700)
    window.setBackground(color_rgb(0, 0, 0))

    r = Rectangle(Point(0,0), Point(50,50))
    r.setFill("white") 
    r.draw(window) 
    time.sleep(1) 
    r.p1 = Point(50,50) 
    r.p2 = Point(100,100)
    #renderBars(window, array)

    window.getMouse()
    window.close()