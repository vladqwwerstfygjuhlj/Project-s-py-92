class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_info(self):

        return f"[{self.year}] {self.make} {self.model}"
car1 = Car("Chevrolet", "Impala", 1967)
car2 = Car("Buick", "Riviera", 1963)

print(car1.get_info())  
print(car2.get_info())  

