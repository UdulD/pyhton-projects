l=[0,1,2,3,4,5,6,7,8,9]

def is_in_list(l,n):
    if len(l)==0:
        return False
    middle=len(l)//2
    if l[middle]==n:
        return True
    elif n<l[middle]:
        return is_in_list(l[:middle],n)
    
    else:
        return is_in_list(l[middle+1:],n)
    

n=int(input('enter n '))
print(is_in_list(l,n))