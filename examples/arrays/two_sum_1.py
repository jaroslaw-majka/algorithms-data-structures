# https://leetcode.com/problems/two-sum/
def two_sum(nums: list[int], target: int) -> list[int]:
    indices = {}

    for index in range(len(nums)):
        if target - nums[index] in indices:
            return [index, indices[target - nums[index]]]

        indices[nums[index]] = index

    return []
