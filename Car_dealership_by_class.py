class Vehicale:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.seating_capacity = None

    def set_seating_capacity(self, seating_capacity):
        self.seating_capacity = seating_capacity

    def display_properties(self):
        print("\n-----------------------------")
        print(f"Car {self.make} Properties:")
        print("Make of the car: ", self.make)
        print("Model of the car: ", self.model)
        print("Year of the car: ", self.year)
        print("Color of the car: ", self.color)
        print("Seating Capacity of the car: ", self.seating_capacity)
        print("--------------------------------")

Vehicale1 = Vehicale("Toyota", "Camry", 2020, "Red")
Vehicale1.set_seating_capacity(5)

Vehicale2 = Vehicale("Honda", "Civic", 2019, "Blue")
Vehicale2.set_seating_capacity(4)

Vehicale3 = Vehicale("Ford", "Mustang", 2021, "Black")
Vehicale3.set_seating_capacity(2)

Vehicale4 = Vehicale("Chevrolet", "Impala", 2018, "White")
Vehicale4.set_seating_capacity(6)

Vehicale1.display_properties()
Vehicale2.display_properties()
Vehicale3.display_properties()
Vehicale4.display_properties()