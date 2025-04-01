class Vehicle:
    def move(self):
        raise NotImplementedError("Subclass must define move()")

class Car(Vehicle):
    def move(self):
        print("Driving on roads! 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying in the sky! ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing on water! ⛵")

# Polymorphism in action
vehicles = [Car(), Plane(), Boat()]
for v in vehicles:
    v.move()


    # Output:
    # Driving on roads! 🚗  
    # Flying in the sky! ✈️  
    # Sailing on water! ⛵  