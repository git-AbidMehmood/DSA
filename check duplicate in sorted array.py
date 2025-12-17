def check_duplicate_two_pointer(arr):
    arr.sort()  # important
    left = 0
    right = 1

    while right < len(arr):
        if arr[left] == arr[right]:
            return True  # duplicate found
        left += 1
        right += 1

    return False

print(check_duplicate_two_pointer([1,2,3,4,5,6,1,2,4]))
