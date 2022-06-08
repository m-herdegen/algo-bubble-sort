
sequence =[5, 4, 3, 2, 1, 0 ] 
# [23, 456, 867, 23, 564, 56, 2,1, 23, 0, 4, 2, 88, 1123, 76]
#[4, 3, 5, 0, 1]

# Your Code Here

def bubble_sort(arr):
    bubble_sort.swaps = 0
    bubble_sort.iterations = 0
    previous = 0
    current = 0
    result = []
    looping = True
    
    while looping:
        bubble_sort.iterations += 1
        swapped = False
        for i in range(len(arr)-1):
            previous = arr[i]
            current = arr[i+1]
            if previous > current:
                bubble_sort.swaps += 1
                swapped = True
                arr[i] = current
                arr[i+1] = previous  
        if not swapped:
            looping = False
            result = arr
    return result

print(f"Final result: {bubble_sort(sequence)}")
print(f"Swaps: {bubble_sort.swaps}")
print(f"Iterations: {bubble_sort.iterations}")
