class Car:
    def __init__(self, fuel_level, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.fuel_level = fuel_level

    def start(self):
        if self.fuel_level < 2:
            print("Not enough fuel level")
        else:
            print("Starting...")

    def add_fuel(self, litre):
        if self.fuel_level + litre <= 25:
            self.fuel_level += litre
            print(f"Fuel level: {self.fuel_level}")
        else:
            print("Maximum fuel level reached")

    def drive(self, distance):
        if distance > self.fuel_level * 10:
            print("Not enough fuel")
        else:
            print('enough fuel')

    def screen(self):
        print(self.brand,self.model,self.year, self.fuel_level,'L')


Car1 = Car(5,'toyota','axio',2014)
Car1.start()
Car1.add_fuel(10)
Car1.drive(15)
Car1.screen()
 