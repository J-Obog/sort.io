from graphics import GraphWin, color_rgb
from random import randint
import bar
import algo

def resolveMethodName(method):
    return ["Bubble Sort", "Insertion Sort", "Selection Sort"][method] 


def sortVisual(method, array):
    winName = resolveMethodName(method)
    window = GraphWin(winName, 700, 700)
    window.setBackground("black")

    bar.renderBars(window, array)
    #algo.bubbleSort(array, window)
    algo.selectionSort(array, window)

    window.getMouse()
    window.close()

if __name__ == "__main__":
    randArr = [ randint(0, 100) for i in range(100)]
    print(randArr)
    sortVisual(0, randArr)