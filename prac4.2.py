# Single and Multiple Inheritance
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    def start(self):
        print(f"{self.brand} {self.model} starts.")
        
class Car(Vehicle):
    def __init__(self, brand, model, seats):
        super().__init__(brand, model)
        self.seats = seats
            
    def honk(self):
        print(f"{self.brand} honks!")

car = Car("Toyota", "Corolla", 5)
car.start()
car.honk()