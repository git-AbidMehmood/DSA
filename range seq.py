def summary_ranges(nums):
    # If list is empty, return empty result
    if not nums:
        return []

    res = []
    start = nums[0]  # starting number of the current range

    # Loop from index 1 to end
    for i in range(1, len(nums)):
        # If current number is not consecutive
        if nums[i] != nums[i - 1] + 1:
            # Close the current range
            if start == nums[i - 1]:
                res.append(f"{start}")
            else:
                res.append(f"{start}->{nums[i - 1]}")
            # Start a new range
            start = nums[i]

    # Add the final range

    if start == nums[-1]:
        res.append(f"{start}")
    else:
        res.append(f"{start}->{nums[-1]}")
    return res


# Example usage:
nums = [0, 1, 2, 4, 5, 6]
print(summary_ranges(nums))
