"""
The Selection Sort code we saw sorts an array from least to greatest.
Modify the code so that the code sorts an array from greatest to least.

Selection Sort Code:

arr  = [?,?,?]#change this array to the array you want to sort
for first_idx in range(len(arr)):
    min_idx = first_idx
    for second_idx in range(first_idx+1, len(arr)):
        if arr[second_idx] < arr[min_idx]:
            min_idx = second_idx
    arr[first_idx], arr[min_idx] = arr[min_idx], arr[first_idx]

"""

# write your code below

arr = [1, 27, 412, 3, 12, 4]
for first_idx in range(len(arr)):
    min_idx = first_idx
    for second_idx in range(first_idx + 1, len(arr)):
        if arr[second_idx] > arr[min_idx]:
            min_idx = second_idx
    arr[first_idx], arr[min_idx] = arr[min_idx], arr[first_idx]
print(arr)
