import random

class Car:
    def __init__(self, model, color):
        self.fuel = random.randrange(0, 9)  # Initialize fuel with random value
        self.trip_distance = 0
        self.model = model
        self.color = color

    def move(self, distance):
        if self.fuel >= distance:
            self.trip_distance += distance
            self.fuel -= distance
            print(f"{self.model} ({self.color}) traveled {distance} units.")
        else:
            print(f"{self.model} ({self.color}) ran out of fuel!")

desired_dist = 50  # Set the desired race distance

# Create 3 car instances
car1 = Car("Ferrari", "red")
car2 = Car("Lamborghini", "yellow")
car3 = Car("Porsche", "blue")

race_dist = 0
while race_dist < desired_dist:
    for car in [car1, car2, car3]:
        moved_distance = random.randrange(0, 9)
        car.move(moved_distance)
        race_dist += moved_distance

        if car.trip_distance >= desired_dist:
            print(f"\n{car.model} ({car.color}) has won the race with a distance of {car.trip_distance}!")
            break  # Exit the loop if a car wins

    if any(car.trip_distance >= desired_dist for car in [car1, car2, car3]):
        break  # Exit the outer loop if any car wins

# Print final results for each car
for car in [car1, car2, car3]:
    print(f"\n{car.model} ({car.color}) traveled {car.trip_distance} units and has {car.fuel} units of fuel remaining.")
