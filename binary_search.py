def binary(arr,n):
    lower=0
    upper=len(arr)-1

    while lower<=upper:
        mid=(lower+upper)//2
        if arr[mid]==n:
            return mid
        
        elif arr[mid]>n:
                upper=mid-1
        else:
            lower=mid+1
            
    return None

arr=[1,2,3,4,5,6,7,8,9,10,11]
n=11

print(binary(arr,n))


