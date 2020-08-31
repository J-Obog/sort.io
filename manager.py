from graphics import Rectangle, Point, color_rgb

# Draw a single bar
def drawBar(window, x1, y1, x2, y2):
    bar = Rectangle(Point(x1, y1), Point(x2, y2)) 
    bar.setFill(color_rgb(255, 255, 255)) 
    bar.draw(window)


# Initially load all bars
def renderBars(window, arr):
    maxVal= max(arr)    
    barWidth = (700/len(arr)) - 5
    for [index, val] in enumerate(arr): 
        x1 = index*barWidth 
        x2 = x1 + barWidth
        y1 = 0 
        y2 = (700*(val/maxVal)) - 5
        drawBar(window, x1, y1, x2, y2)

#remove