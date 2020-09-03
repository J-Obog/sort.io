import algorithms 

algoInfo = [
    {
        "name": "Bubble Sort", 
        "complexity": "O(n^2)"
    },
    {
        "name": "Insertion Sort", 
        "complexity": "O(n^2)"
    },
    {
        "name": "Selection Sort", 
        "complexity": "O(n^2)"
    }
]

algoMapper = {
    0: algorithms.bubbleSort,
    1: algorithms.insertionSort,
    2: algorithms.selectionSort
}