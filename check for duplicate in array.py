def containsDuplicate(nums):
    seen = set()

    for num in nums:
        if num in seen:
            return True
        print(seen)
        seen.add(num)
    print(seen)
    return False
numbers = [1,2,3,4]
print (containsDuplicate(numbers))
