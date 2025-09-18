stack=[]

def push(x):
    stack.append(int(input('enter x ')))

def pop(x):
    if len(stack)==0:
        print('stack is emty')
    else:
        stack.pop()

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
    choice = input("Enter your choice: ")

    if choice == "push":
        push(x)
    elif choice == "pop":
        pop(x)
    elif choice == "peek":
        peek(x)
    elif choice == "dis":
        display(x)
    elif choice == "exit":
        print('exiting')
        break
        


