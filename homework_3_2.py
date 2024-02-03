# черновой вариант
import random



class Car:
    def __init__(self, model, color):
        """
        Функція є конструктором класу.Призначена для ініціалізації об'єкта класу з заданими параметрами.
        :param model:
        :param color:
        """
        self.fuel = random.randrange(0, 9)  # Initialize fuel with random value
        self.trip_distance = 0
        self.model = model
        self.color = color

    def move(self, distance):
        """
        Функція призначена для моделювання переміщення автомобіля на визначену відстань
        :param distance:
        :return: Повертає True, щоб показати успішну подорож,Повертає False, щоб показати,
        що подорож не відбулася через нестачу пального.
        """
        if self.fuel >= distance:
            self.trip_distance += distance
            self.fuel -= distance
            print(f"{self.model} ({self.color}) проїхала {distance} км.")
        else:
            print(f"{self.model} ({self.color}) не має палива!")

desired_dist = 10

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
    print(f"\n{car.model} ({car.color}) проїхала {car.trip_distance} км та має {car.fuel} одиниць палива.")
