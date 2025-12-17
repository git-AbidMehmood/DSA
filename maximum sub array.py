"""Given an integer array nums, find the subarray with the largest
 sum, and return its sum.
 Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
 Output: 6
 Explanation: The subarray [4,-1,2,1] has the largest sum 6."""

def maxSubArray(nums):
    current_sum = 0
    max_sum = nums[0]

    for num in nums:
        current_sum += num
        max_sum = max(max_sum, current_sum)
        if current_sum < 0:
            current_sum = 0

    return max_sum

nums = [-2,1,-3,4,-1,2,1,-5,4]
print("max sum", maxSubArray(nums))
