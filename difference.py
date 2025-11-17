nums=[1,2,3,6,8,9,2]
k=0

def dif():
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if abs(nums[i]-nums[j])==k:
                print(nums[i], ',',nums[j])


results=dif()
print(results)