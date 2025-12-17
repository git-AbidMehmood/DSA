def find_target_sum(arr, target):
    left = 0
    right = len(arr)-1
    res = []
    while left < right :
        if arr[left] + arr[right] == target:
            res.append((arr[left],arr[right]))
            left +=1
            right -=1
        elif arr[left] + arr[right] <  target:
            left +=1
        else :
            arr[left] + arr[right] > target
            right -=1
    return res

print(find_target_sum([1,2,3,4,5,6,7,8], 8))

