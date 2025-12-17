"""
Problem Statement:
Given an array of positive integers nums and a target S, find the length of the smallest contiguous subarray
whose sum is greater than or equal to S.
Return 0 if no such subarray exists.


Input: nums = [2,3,1,2,4,3], S = 7
Output: 2
Explanation: The subarray [4,3] has sum = 7, which is the smallest length.
"""
def SmallestContiguousSubarray(arr , s):
    current_sum =0
    min_len = float('inf')
    left = 0
    for right in range (len(arr)):
        current_sum += arr[right]
        while current_sum >= s :
            min_len = min( right - left + 1, min_len)
            current_sum -= arr[left]
            left += 1
    if min_len == float('inf'):
        return 0
    return min_len

print (SmallestContiguousSubarray([2,3,1,2,4,3],7))
