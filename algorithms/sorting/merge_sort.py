def merge_sort(arr):
    '''
        Merge Sort algorithm for sorting arrays.
        Merge sort is splitting array in 2 untill the base cas eis met (1 or no
        items in the array), and then merges the arrays together.

        This method sorts the array in-place, meaning that it does not return a
        new array object, but sorts the initial array.

        The complexity of merge sort algorithm is O(n log n), where `n` is the
        number of elements in the array
    '''
    if len(arr) > 1:
        # Divide the array into two halves
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursively sort both halves
        merge_sort(left_half)
        merge_sort(right_half)

        # Merge the sorted halves
        i = j = k = 0

        # Copy data to temp arrays left_half[] and right_half[]
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Check if any element was left
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1



if __name__ == '__main__':
    # Example usage
    unsorted_array = [38, 27, 43, 3, 9, 82, 10]
    merge_sort(unsorted_array)
    print("Sorted array:", unsorted_array)
