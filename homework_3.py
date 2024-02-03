import random

class Car:
    def __init__(self, model , color):
        self.fuel = random.randrange(0, 9)
        self.trip_distance = 0
        self.model = model
        self.color = color
    def move(self, distance):
        if self.fuel >= distance:
            self.fuel -=distance
            return True
        else:
            print(f"Недостатньо пального для проїзду {distance} км.")
            return False


car_1 = Car('Mercedes', 'black',  )
car_2 = Car('Audi', 'pink')
car_3 = Car('BMW', 'white')

desired_dist = 100
race_dist = 0

while race_dist < desired_dist:

    for car in [car_1, car_2, car_3]:
        distance = random.randrange(0, 9)
        path = car.move(distance)
        if path:
            race_dist += distance
            print(f"{car.color} {car.model} проїхав {distance} км. Загальна відстань: {race_dist} км.")
            if race_dist >= desired_dist:
                print(f"\n{car.color} {car.model} переміг! Відстань: {car.trip_distance} км.")
                break

        #
for car in [car_1, car_2, car_3]:
    print(f"\n{car.color} {car.model}:")
    print(f"  Пройдена відстань: {car.trip_distance} км.")
    print(f"  Запас палива: {car.fuel} одиниць.\n")



