from random import randint


def quick_sort(arr: list) -> list:
    """
        Quicksort algorithm applies the divide-and-conquer principle to divide
        the input array into two lists, the first list with small items and the
        second with large items.
        The algorithm then sorts the lists recursively.


        This method sorts the array in-place, meaning that it does not return a
        new array object, but sorts the initial array.

        The complexity of Quick Sort algorithm is O(n log_2 n)
    """
    # Base case when array contains less than 2 elements
    if len(arr) < 2:
        return arr

    low, same, high = [], [], []

    # Randomly create pivot element from the initial array
    pivot = arr[randint(0, len(arr) - 1)]

    # Iterate and assign values to `low`, `same` and `high` arrays
    for item in arr:
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        else:
            high.append(item)

    # Recursively combine the arrays for the final result
    return quick_sort(low) + same + quick_sort(high)


if __name__ == '__main__':
    unsorted_array = [1, 4, 2, 8, 5]
    sorted_array = quick_sort(unsorted_array)
    print(unsorted_array)
    print(sorted_array)
