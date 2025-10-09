class Queue:
    def __init__(self,elements=None):
        if elements is None:
            self.elements=[]
        else:
            self.elements=elements

    def add(self):
        x=int(input('enter the value u wanna add '))
        self.elements.append(x)
    
    def peek(self):
        print(self.elements[0])

    def pop(self):
        if len(self.elements)==0:
            print('emty queue')
        else:
            self.elements.pop(0)

    def display(self):
        if len(self.elements)==0:
            print('emty queue')
        else:
            print(self.elements)

    def exit(self):
        print('exiting...')

Queue1=Queue([1,2,3])
Queue2=Queue([11,9])

receiver_choice=input('select Queue (1/2)')
if receiver_choice=='1':
    receiver=Queue1
elif receiver_choice=='2':
    receiver=Queue2
else:
    print('invalid choice :(')


while True:
        choice=str(input('enter your choice '))
        if choice=='add':
            receiver.add()           
        elif choice=='pop':
            receiver.pop()
        elif choice=='dis':
            receiver.display()
        elif choice=='peek':
            receiver.peek()
        elif choice=='exit':
            receiver.exit()
            break
        else:
            print('invalid command')
        

        