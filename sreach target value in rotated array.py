from typing import List

def searchRotated(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        # Check if left half is sorted
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:  # Right half is sorted
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1  # target not found


nums = [4, 5, 6, 7, 0, 1, 2]
target = 0

print(searchRotated(nums, target))  # Output: 4

target = 3
print(searchRotated(nums, target))  # Output: -1
