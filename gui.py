from graphics import GraphWin, color_rgb
from random import randint
import bar

def resolveMethodName(method):
    return ["Bubble Sort", "Insertion Sort", "Selection Sort"][method] 


def sortVisual(method, array, graphBg="black", barColor="white"):
    winName = resolveMethodName(method)
    window = GraphWin(winName, 700, 700)
    window.setBackground(graphBg)

    bar.renderBars(window, array, barColor)

    

    window.getMouse()
    window.close()

if __name__ == "__main__":
    randArr = [ randint(0, 100) for i in range(5)]
    print(randArr)
    sortVisual(0, randArr)