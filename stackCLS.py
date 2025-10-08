class Stack:
    def __init__(self,elements=None):
        if elements is None:
            self.elements=[]
        else:
            self.elements=elements
        

    def add(self):
        x=input('enter the value u wanna add ')
        self.elements.append(x)

    def peek(self):
        print(self.elements[-1])
    
    def pop(self):
        self.elements.pop(-1)

    def display(self):
        print(self.elements)

    def exit(self):
        print('exiting')
        
stack1=Stack([1,3,5,8])
stack2=Stack([2,4,6])

receiver_choice = input("Select your stack (1 or 2): ")
if receiver_choice== '1':
    receiver=stack1
elif receiver_choice== '2':
    receiver=stack2


while True:
    choice = str(input('enter your choice '))
    
    if choice=='add':
        receiver.add()
    elif choice=='peek':
        receiver.peek()
    elif choice=='pop':
        receiver.pop()
    elif choice=='dis':
        receiver.display()
    elif choice=='exit':
        receiver.exit()
        break
    


