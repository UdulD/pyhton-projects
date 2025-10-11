def  mergesort(a_list):
    if len(a_list) <= 1:
        return a_list
    mid = len(a_list) // 2
    left_half=a_list[:mid]
    right_half=a_list[mid:]
    left_half=mergesort(a_list[:mid])
    right_half=mergesort(a_list[mid:])
    
    i=0
    j=0
    k=0

    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            a_list[k]=left_half[i]
            i=i+1
        else:
            a_list[k]=right_half[j]
            j=j+1
        k=k+1
    
    while i < len(left_half):
        a_list[k]=left_half[i]
        i=i+1
        k=k+1
    while j < len(right_half):
        a_list[k]=right_half[j]
        j=j+1
        k=k+1
    return a_list

a_list=[38, 27, 43, 3, 9, 82, 10]
print(a_list)
print(mergesort(a_list))