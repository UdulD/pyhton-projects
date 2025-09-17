def GCD(a,b):
    if a>b:
        n=a//b
        c=a-n*b
        if c==0:
            return b
        return GCD(b,c)
    else:
        n=b//a
        c=b-n*a  
        if c==0:
            return a
        return GCD(a,c)

a = int(input('enter a: '))
b = int(input('enter b: '))

print(GCD(a,b))
