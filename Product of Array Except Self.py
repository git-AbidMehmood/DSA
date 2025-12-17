def productExceptSelf(nums):
    n = len(nums)
    answer = [1] * n
    print(answer)
    # STEP 1: Left products
    left = 1
    for i in range(n):
        answer[i] = left
        left *= nums[i]
        print("left", left)
            # STEP 2: Right products
    print("left", answer)
    right = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= right
        right *= nums[i]
        print("right", right)
    print("right", answer)
    return answer

numbers =  [1,2,3,4]
print(productExceptSelf(numbers))