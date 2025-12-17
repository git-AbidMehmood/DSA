def twosum(number,target):
    seen= {}
    for i, num in enumerate(number):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num]=i

number = [7,1 ,6, 3]
target= 9
print(twosum(number, target))



