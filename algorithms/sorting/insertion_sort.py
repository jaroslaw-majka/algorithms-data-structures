def insertion_sort(arr):
    """
        Insertion Sorting algorithm.
        You can think as this algorithm splits the array in two parts.
        Left part is already sorted, while right part is not yet touched.
        With each iteration it picks one element and puts it in place on
        the left side of the array.

        This method sorts the array in-place, meaning that it does not return a
        new array object, but sorts the initial array.

        The complexity of Insertion Sort algorithm is O(n^2)
    """
    # Start at the second element of the array
    for idx in range(1, len(arr)):
        current_item = arr[idx]

        # Initialize a variable that will be used to find the correct
        # position of the `current_item`
        j = idx - 1

        # Iterate through the left side of the array shifting
        # values one index to the right.
        while j >= 0 and arr[j] > current_item:
            arr[j + 1] = arr[j]
            j -= 1

        # Place `current_item` in it's correct place.
        arr[j + 1] = current_item

    return arr
