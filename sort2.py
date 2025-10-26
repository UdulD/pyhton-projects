def sort(arr):
    n=len(arr)
    result=[arr[0]]
    for i in range(1,n):
        if arr[i]>result[-1]:
            result.append(arr[i])

    return result

nums=[7,3,2,4,8,5,6,9,7,10,2,11,5]

print(sort(nums))
    
