from graphics import *
from random import randint
from interface import GraphInterface, StatInterface
import constants

def main():
    try:
        sortMethod = int(input("Method: ")) 
        #Check for method-based problems
        if sortMethod < 0 or sortMethod > 2:
            raise Exception("Sorting method must be valid")

        minVal = int(input("Min: ")) 
        maxValue = int(input("Max: "))

        #Check for range-based errors
        if minVal > maxValue:
            raise Exception("Minimum value cannot be greater than maximum value")
        elif minVal == maxValue:
            raise Exception("Minimum value cannot be equal to maximum value")
    
        arrLength = int(input("Generations: ")) 
        
        #Check for array-based errors
        if arrLength < 0:
            raise Exception("Array length cannot be negative") 
        elif arrLength == 0:
            raise Exception("Array cannot be empty") 
        elif arrLength < 2:
            raise Exception("Array must have at least two values") 

        refreshRate = float(input("Refresh Rate: "))  

        randArray = [ randint(minVal, maxValue) for i in range(arrLength) ] 
        visualizeSort(sortMethod, randArray, refreshRate)
    except Exception as e:
        print(type(e))
        print(e)




def visualizeSort(method, arr, refRate):
    sortWin = GraphWin("Sorting Algorithm", 700, 700)
    sortWin.setBackground("black")

    statWin = GraphWin("Stats", 300, 300) 
    statWin.setBackground("black")

    graphInterface = GraphInterface(sortWin, arr, refRate) 
    statsInterface = StatInterface(statWin, constants.algoInfo[method])
    constants.algoMapper[method](arr, graphInterface, statsInterface)


    sortWin.getMouse()
    sortWin.close()

if __name__ == "__main__":
    main()