class Bank_acc:
    def __init__(self,id,owner,balance):
        self.id=id
        self.owner=owner
        self.balance=balance

    def deposit(self,amount):
        self.balance+=amount
        print()
        print(amount,'Rs','has been credited')
        print('avalible balance :',self.balance)
        print()

    def withdraw(self,amount):
        if amount>self.balance:
            print('Insufficient funds!')
        else:
            self.balance-=amount
            print(amount,'Rs','has been debited')
            print('avalible balance :',self.balance)
        print()

    def rem_balance(self):
        print()
        print('avalible balance is',self.balance,'at the time this message generated')
        print()

    def display(self):
        print(self.id,'   ',self.owner)
        print('remaining bank balance is',self.balance)
        print()

    def transfer(self,receiver,amount):
        if amount>self.balance:
            print('Insufficient balance!')
        else:
            self.balance-=amount
            receiver.balance+=amount
            print('transfer successful!','remaining balance is',self.balance)





boc=Bank_acc('101','udul',100)
boc.deposit(100)


com=Bank_acc('102','dilsara',500)
com.deposit(150)
com.withdraw(100)
com.display()

com.transfer(boc,500)

boc.display()
com.display()
        