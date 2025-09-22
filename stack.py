stack=[]

def add(x):
    stack.append(int(input('enter value u wanna add ')))

def pop(x):
    if len(stack)==0: 
        print('emty stack')
    else:
        stack.pop(-1)

def peek(x):
    if len(stack)==0:
        print('emty stack')
    else:
        print(stack[-1])
    
def display(x):
    if len(stack)==0:
        print('emty stack')
    else:
        print(stack)
 
x=True
while True:
    choice =input('enter your choice ')
    if choice== 'add':
        add(x)
    elif choice=='pop':
        pop(x)
    elif choice=='peek':
        peek(x)
    elif choice=='dis':
        display(x)
    elif choice=='exit':
        break
    else:
        print('invalid choice')

        


