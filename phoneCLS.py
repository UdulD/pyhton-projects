class Phone:
    def __init__(self,storage,battery):
        self.storage=storage
        self.battery=battery

    def charge(self,time):
        battery_pctg=self.battery + time/5
        if battery_pctg>=100:
            print('fully charged 100%')
        else:
            self.battery=battery_pctg
            print('Battery percentage:',battery_pctg,'%')

    def install(self, app_size):
        if self.battery < 5:
            print("Please connect phone to the charger")
            return  

        elif self.storage < app_size:
            print("Not enough space :(")
        else:
            self.storage -= app_size
            print("App installed successfully")
            print("Remaining space:", self.storage,"GB")

    def need_to_charge(self):
        if self.battery<=10:
            print('Low battery')
        else:
            print("Battery OK")

    def display(self):
        print(self.battery,'%',"  ",self.storage,'GB','space remaining'  )

    

    







apple=Phone(512,10)
apple.charge(10)
apple.install(200)
apple.need_to_charge()
apple.display()




        

        

        