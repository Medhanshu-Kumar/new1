# quicksort algorithm
def quicksort(arr):
    if len(arr) <=1 :
        return arr
    pivot = arr[-1]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x== pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)
arr = [10, 7, 8, 9, 1, 5]
sorted_arr = quicksort(arr)
print(sorted_arr)



