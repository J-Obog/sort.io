from graphics import Rectangle, Point, Text
from time import sleep

class StatInterface:
    def __init__(self, win, info):
        center = win.getWidth()/2
        self.numOfSwaps = 0
        #Create objects
        self.algoName = Text(Point(center, 10), f'Method: {info["name"]}') 
        self.timeComplexity = Text(Point(center, 40), f'Time Complexity: {info["complexity"]}')
        self.swaps = Text(Point(center, 70), f'Swaps: {self.numOfSwaps}')
        
        #Style objects
        self.styleText(self.algoName, self.timeComplexity, self.swaps)

        #Render objects
        self.renderText(win, self.algoName, self.timeComplexity, self.swaps)


    def styleText(self, *items):
        for item in items:
            item.setTextColor("white")

    def renderText(self, win, *items):
        for item in items:
            item.draw(win)

    def updateSwaps(self):
        self.numOfSwaps += 1
        self.swaps.setText(f'Swaps: {self.numOfSwaps}')
        pass


class GraphInterface:
    def __init__(self, win, arr, refreshRate=0.5):
        self.win = win
        self.winHeight = win.getHeight()
        self.winWidth = win.getWidth()
        self.barWidth = self.winWidth/len(arr)
        self.maxVal = max(arr)
        self.refreshRate = refreshRate
        self.renderBars(arr)

    def calculateBarCoords(self, index, value):
        x1 = index*self.barWidth
        x2 = x1 + self.barWidth
        y1 = self.winHeight
        y2 = (self.winHeight*(1-(value/self.maxVal))) + 5
        return x1, y1, x2, y2
        
    def drawBar(self, coords, color="white"):
        x1, y1 = coords[:2]
        x2, y2 = coords[2:]
        bar = Rectangle(Point(x1, y1), Point(x2, y2)) 
        bar.setFill(color) 
        bar.draw(self.win) 
        
    def renderBars(self, arr, swapArr=[]):
        for [index, value] in enumerate(arr): 
            coords = self.calculateBarCoords(index, value)
            color = "red" if index in swapArr else "white"
            self.drawBar(coords, color)

    def rerender(self, arr, swapArr):
        sleep(self.refreshRate)
        for item in self.win.items[:]:
            item.undraw()
        self.win.update()
        self.renderBars(arr, swapArr)