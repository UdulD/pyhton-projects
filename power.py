n=int(input('enter n:'))
i=int(input('enter i:'))
def power(n,i):
    if i==0: return 1
    elif i==1: return n
    elif i>1:
        if i%2==0: return (power(n,i/2))**2
        else: return (power(n,(i-1)/2))**2*n

print()
print(n,'**',i,'=',power(n,i))
