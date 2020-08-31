from graphics import *
from random import randint
from gui import sortVisual


def main(): 
    randArr = lambda min=0, max=100, N=50: [ randint(min, max) for i in range(N)]

    algo = int(input("Choose a sorting method [Bubble=0, Insertion=1, Selection=2]: ")) 
    arr = randArr()

    try:
        if not(algo >= 0 and algo <= 2): 
            raise Exception("Hello World")
        sortVisual(algo, arr)
    except Exception as err: 
        print(err)
    

if __name__ == "__main__":
    main()
