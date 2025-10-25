# insertion_sort_descending.py

def insertion_sort_desc(arr):
    # Loop through all elements
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Move elements that are smaller than key one position ahead
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key

# Example usage
data = [4, 3, 14, 7, 3, 6]
print("Original array:", data)
insertion_sort_desc(data)
print("Sorted array (decreasing):", data)
