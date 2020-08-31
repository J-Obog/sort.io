from graphics import *

class ResizeableGraphWin(GraphWin):

    """ A resizeable toplevel window for Zelle graphics. """

    def __init__(self, title="Graphics Window", width=200, height=200, autoflush=True):
        super().__init__(title, width, height, autoflush)
        self.pack(fill="both", expand=True)  # repack?

    def resize(self, width=200, height=200):
        self.master.geometry("{}x{}".format(width, height))
        self.height = int(height)
        self.width = int(width)

# test code

win = ResizeableGraphWin("My Circle", 100, 100)
win.setBackground('green')

c = Circle(Point(75, 75), 50)
c.draw(win)  # should only see part of circle

win.getMouse() # pause for click in window

win.resize(200, 400)  # should now see all of circle

win.getMouse() # pause for click in window

c.move(25, 125)  # center circle in newly sized window

win.getMouse() # pause for click in window

c.setFill('red')  # modify cirlce

win.getMouse() # pause for click in window

win.close()