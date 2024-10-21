def two_sum(arr: list, target: int):
    '''
        Two pointer technique is useful when you need to work on two elements
        of an array. It is a popular interview question.
    '''

    # Sorting helps for using two-pointer technique
    # Because if the sum is higher than target, we know
    # that we should move the right pointer to the next item.
    # Otherwise leave right pointer, where it is, and move
    # left pointer
    arr.sort()

    # left starts at the first element of the array
    # right starts at the last element of the array
    left, right = 0, len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return (arr[left], arr[right])
        if current_sum < target:
            left += 1
        else:
            right -= 1
    return None


if __name__ == '__main__':
    # Example usage
    test_arr = [10, 2, 3, 6, 7, 9]
    target_sum = 9
    print(two_sum(test_arr, target_sum))  # Output: (2, 7)
