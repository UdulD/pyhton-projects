def is_palindromic(n):
    if len(n)==1:
        return True
    elif n[0]!=n[-1]:
        return False
    else:
        return is_palindromic(n[1:-1])



n=str(input('enter n: '))
print(is_palindromic(n))
        
