from typing import List


def findMin(nums: List[int]) -> int:
    """
    Find the minimum element in a rotated sorted array.

    Args:
    nums: List[int] - rotated sorted array
    [0 1 2 3 4 5]
    [5 0 1 2 3 4 ]
    [4 5 0 1 2 3]
    Returns:
    int - minimum element
    """
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        if nums[mid] > nums[right]:
            # Minimum must be in the right half
            left = mid + 1
        else:
            # Minimum could be mid or in the left half
            right = mid

    return nums[left]
nums = [4, 5, 6, 7, 0, 1, 2]
print(findMin(nums))  # Output: 0

nums2 = [3, 4, 5, 1, 2]
print(findMin(nums2))  # Output: 1
