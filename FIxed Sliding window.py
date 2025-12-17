#fixed sliding window


def fixedwindowformaxsum(arr,k, t):
    left = 0
    current_sum  = 0
    max_sum = float('-inf')
    count = 0;

    for i in range (len(arr)):
        current_sum += arr[i]
        if arr[i] < 0:
            count+=1
        if (i -left + 1 ) == k:
            if count <=t:
                max_sum = max (max_sum, current_sum)
            if arr[left] < 0:
                count -= 1
            current_sum -= arr[left]
            left += 1
    return max_sum

print(fixedwindowformaxsum( [4, -1, 2, 1, -3, 5, -2] , 3, 1))
