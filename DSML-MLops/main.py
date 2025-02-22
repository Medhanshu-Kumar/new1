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

def merge_sort(arr):
    if len(arr) <= 1:
        return arr  # Base case: Already sorted
    
    # Step 1: Divide
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])  # Recursively sort left half
    right_half = merge_sort(arr[mid:])  # Recursively sort right half
    
    # Step 2: Merge sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    sorted_list = []
    i = j = 0
    
    # Compare elements from both halves and merge in sorted order
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
    
    # Add any remaining elements
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    
    return sorted_list

# Example usage
arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort(arr)
print(sorted_arr)  # Output: [3, 9, 10, 27, 38, 43, 82]

# add insert_sort logo
def insertion_sort_main_branch(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

arr = [5, 3, 8, 6, 2]
insertion_sort(arr)
print("Sorted Array:", arr)

##learning how to pull changes

