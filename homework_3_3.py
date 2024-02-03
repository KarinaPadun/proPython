import random


class Car:
    def __init__(self, model, color):
        """
        Функція є конструктором класу.Призначена для ініціалізації об'єкта класу з заданими параметрами.
        :param model:
        :param color:
        """
        self.fuel = random.randrange(0, 9)
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
            self.fuel -= distance
            self.trip_distance += distance
            return True
        else:
            print(f"{self.color} {self.model} не має достатньо пального для проїзду {distance} км.")
            return False


car_1 = Car('Mercedes', 'Black')
car_2 = Car('Audi', 'Pink')
car_3 = Car('BMW', 'White')

desired_dist = 10
race_dist = 0

while race_dist < desired_dist:
    fuel_empty = True
    for car in [car_1, car_2, car_3]:
        distance = random.randrange(0, 9)
        path = car.move(distance)
        if path:
            race_dist += car.trip_distance
            print(f"{car.color} {car.model} проїхав {distance} км. Загальна відстань: {race_dist} км.")
            if race_dist >= desired_dist:
                print(f"\n{car.color} {car.model} переміг!")
                break

            if car.fuel > 0:
                fuel_empty = False

    if fuel_empty:
        print("\nЗакінчилося пальво для всіх машин.")
        break

for car in [car_1, car_2, car_3]:
    print(f"\n{car.color} {car.model}:")
    print(f"  Пройдена відстань: {car.trip_distance} км.")
    print(f"  Запас палива: {car.fuel} одиниць.\n")

