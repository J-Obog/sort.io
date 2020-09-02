from graphics import Rectangle, Point

def calculateBarCoords(context, index, value, maxValue, numOfBars):
    cHeight = context.getHeight()
    cWidth = context.getWidth()
    barWidth = (cWidth/numOfBars)
    x1 = index*barWidth
    x2 = x1+barWidth
    y1 = cHeight
    y2 = (cHeight*(1-(value/maxValue))) + 5
    return x1, y1, x2, y2

def drawBar(context, coords):
    x1, y1 = coords[:2]
    x2, y2 = coords[2:]
    bar = Rectangle(Point(x1, y1), Point(x2, y2)) 
    bar.setFill("white") 
    bar.draw(context)

def renderBars(context, array):
    maxNum = max(array)
    arrayLength = len(array)
    for [index, value] in enumerate(array): 
        coords = calculateBarCoords(context, index, value, maxNum, arrayLength)
        drawBar(context, coords)