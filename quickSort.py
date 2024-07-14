def quickSort(arr):
    pivot = arr[0]
    left = []
    middle = []
    right = []

    for x in arr:
        if x < pivot:
            left.append(x)
        elif x == pivot:
            middle.append(x)
        else:
            right.append(x)
    
    return left + middle + right

import sys

input = sys.stdin.read
data = input().splitlines()

n = int(data[0])
arr = list(map(int, data[1].split()))

result = quickSort(arr)
print(' '.join(map(str, result)))
