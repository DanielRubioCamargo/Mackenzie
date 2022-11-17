def bubbleSort(arr):
    n = len(arr)
    swapped = False

    for i in range(n-1):
        for j in range(0, n-i-1):

            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if not swapped:
            return

arr = [64, 34, 25, 12, 22, 11, 90,4,5,234,456,456,4,65,4,632,45,1,234,53,345,3,8,234,6,1,3,4,33,63,34,4,5,23,123,45,111,
10, 7, 8, 9, 1, 5, 10, 7, 8, 9, 1, 5,10, 7, 8, 9, 1, 5,10, 7, 8, 9, 1, 5,10, 7, 8, 9, 1, 5,10, 7, 8, 9, 1, 5,10, 7, 8, 9, 1, 5,
10, 7, 8, 9, 1, 5,10, 7, 8, 9, 1, 5,10, 7, 8, 9, 1, 5,10, 7, 8, 9, 1, 3, 78,45,23]

bubbleSort(arr)

print(arr)