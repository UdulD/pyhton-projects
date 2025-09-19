queue=[]

def add(x):
    queue.append(int(input('enter value u wanna add ')))

def remove(x):
    if len(queue)==0:
        print('emty queue')
    else:
        queue.pop(0)

def peek(x):
    if len(queue)==0:
        print('emty queue')
    else:
        print(queue[0])

def display(x):
    if len(queue)==0:
        print('emty queue')
    else:
        print(queue)

x=True

while True:
    choice=input('enter your choice ')
    if choice=='add':
        add(x)
    elif choice=='remove':
        remove(x)
    elif choice=='exit':
        print('exiting')
        break
    elif choice=='peek':
        peek(x)
    elif choice=='dis':
        display(x)
