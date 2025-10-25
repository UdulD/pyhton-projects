def selection(arr):
    for i in range(len(arr)):
        min= i

        for j in range(i+1,len(arr)):
            if arr[j]<arr[min]:
                min=j
        if min!=i:
            arr[min],arr[i]=arr[i],arr[min]

    return arr

arr=[2,4,1,5,3,6]

print(selection(arr))