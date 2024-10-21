'''
    The prefix sum technique is useful when you need to calculate the sum of
    any subarray multiple times. Instead of recalculating the sum from scratch
    you can use a precomputed array of prefix sums.
'''
def prefix_sum(arr):
    '''
        Creates a prefix_sum list.
        
        Example input: `[1, 2, 3]`
        Expected output: `[1, 3, 6]`
    '''
    prefix = [0] * (len(arr))
    prefix[0] = arr[0]
    for i in range(1, len(arr)):
        prefix[i] = prefix[i - 1] + arr[i]
    return prefix

def subarray_sum(arr, i, j):
    '''
        Slices the prefixed array and calculates subarray sum
    '''
    prefix = prefix_sum(arr)
    if i == 0:
        return prefix[j]
    return prefix[j] - prefix[i - 1]

# Example usage
test_arr = [1, 2, 3, 4, 5]
subarr_start, subarr_end = 1, 3  # Subarray [2, 3, 4]
print(subarray_sum(test_arr, subarr_start, subarr_end))  # Output: 9
