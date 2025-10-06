def insertion(l):
    for i in range(1,len(l)):
        key=l[i]
        j=i-1


        while j>=0 and l[j]>key:
            l[j+1]=l[j]
            j-=1
        l[j+1]=key

    return l

l=[1,4,5,2,9,7,3]
print(insertion(l))