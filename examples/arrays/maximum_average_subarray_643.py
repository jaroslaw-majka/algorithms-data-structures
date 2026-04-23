# https://leetcode.com/problems/maximum-average-subarray-i/description/

def find_max_average(nums: list[int], k: int) -> float:
    current_sum = sum(nums[:k])

    average = current_sum / k

    left = 0
    for i in range(k, len(nums)):
        current_sum += nums[i]
        current_sum -= nums[left]

        left += 1

        current_average = current_sum / k
        average = max(average, current_average)

    return average
