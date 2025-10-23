def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        # Flag to check if any swapping happened
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap if elements are in wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If no swapping happened, list is already sorted
        if not swapped:
            break

# Example use
nums = [64, 34, 25, 12, 22, 11, 90]
print("Before sorting:", nums)
bubble_sort(nums)
print("After sorting:", nums)



