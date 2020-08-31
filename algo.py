#BUBBLE 
def bubbleSort(arr):
    for i in range(len(arr) - 1, 0, -1):
        for j in range(0,i,1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

#INSERTION
def insertionSort(arr):
    for i in range(1, len(arr), 1):
        for j in range(i, 0, -1):
            if arr[j] < arr[j - 1]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
            else:
                break
#SELECTION 
def selectionSort(arr):
    for i in range(0, len(arr), 1):
        min = i
        for j in range(i, len(arr), 1):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]
