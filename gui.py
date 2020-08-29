from graphics import *
from win32api import GetSystemMetrics

#print(__name__)

def main():
    WINDOW = GraphWin("Aglo Visual", 500, 500)
    WINDOW.setBackground(color_rgb(5,5,5))


    WINDOW.getMouse()
    WINDOW.close() 

if __name__ == "__main__":  
    main()
    print("Running module directly") 
elif __name__ == "gui": 
    main() 