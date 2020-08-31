from graphics import *
from random import randint
from time import sleep
import algos

# Window configuration
ROOT_WIDTH = 700
ROOT_HEIGHT = 700
ROOT_BG = "black"


def rerenderWindow(context, arr):
    #sleep(0.05)
    clearWindow(context)
    renderBars(context, arr)


def clearWindow(win): 
    for item in win.items[:]:
        item.undraw()
    win.update()


def drawBar(context, x1, y1, x2, y2):
    bar = Rectangle(Point(x1, y1), Point(x2, y2)) 
    bar.setFill("white") 
    bar.draw(context)

def renderBars(context, arr):
    maxVal= max(arr)
    
    barWidth = (ROOT_WIDTH/len(arr))- 5
    for [index, val] in enumerate(arr): 
        x1 = index*barWidth 
        x2 = x1 + barWidth
        y1 = 0 
        y2 = (ROOT_HEIGHT * (val/maxVal)) - 5
        drawBar(context, x1, y1, x2, y2)



def main():
    #Set up canvas
    WINDOW = GraphWin("Aglo Visual", ROOT_WIDTH, ROOT_HEIGHT)
    WINDOW.setBackground(ROOT_BG)
     
    randomArray = lambda min=0, max=100, N=50: [ randint(min, max) for i in range(N)]

    rarray = randomArray(0, 100, 10)
    
    renderBars(WINDOW, rarray)
    #WINDOW.items = []
    #WINDOW.flush()

    #algos.bubbleSort(rarray, WINDOW, rerenderWindow)

    
    WINDOW.getMouse()   
    WINDOW.close() 


if __name__ == "__main__":  
    main()
    print("Running module directly") 
elif __name__ == "gui": 
    main() 