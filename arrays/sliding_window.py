def max_sum_subarray(arr, k):
    '''
        This function searches for maximum sum of a subarray of size `k`

        The sliding window technique is useful for finding subarrays 
        that meet certain criteria.

        Usually with this technique you initialize starting window with it's
        values, and then iterate through the iterable, starting from `k`-th
        element
    '''
    # Initialize window sum
    # Basically get the sum of first `k` elements of an array
    max_sum = current_sum = sum(arr[:k])

    # In previous step we initialized sum of first `k` elements
    # of an array, now we start to iterate from `k`-th element
    for i in range(k, len(arr)):
        # Slide the window by one
        # We add current element of the list
        # We remove the element of `[i - k]` from the sum
        current_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, current_sum)
    return max_sum

# Example usage
test_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
window_size = 3
print(max_sum_subarray(test_arr, window_size))  # Output: 24 (subarray [7, 8, 9])
