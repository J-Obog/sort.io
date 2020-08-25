import random 
from unittest import TestCase

def bubbleSort(arr):
    for i in range(len(arr) - 1, 0, -1):
        for j in range(0,i,1):
            if arr[j] > arr[j + 1]:
                tmp = arr[j + 1] 
                arr[j + 1] = arr[j] 
                arr[j] = tmp


def insertionSort(arr):
    for i in range(1, len(arr), 1):
        for j in range(i, 0, -1):
            if arr[j] < arr[j - 1]:
                tmp = arr[j - 1] 
                arr[j - 1] = arr[j] 
                arr[j] = tmp
            else:
                break


def selectionSort(arr):
    for i in range(0, len(arr), 1):
        for j in range(i, len(arr), 1):
            
            pass




randArr = lambda num = 5: [1,9,4,0,2,1]
#bubbleSort(randArr())
#insertionSort(randArr())
selectionSort(randArr())
