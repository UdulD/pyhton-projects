nums = [1,2,3,6,8,9,2]
k = 2

def dif():
    pairs=[]
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if abs(nums[i] - nums[j]) == k:
                pairs.append((nums[i],nums[j]))

    return pairs

    

print(dif())
