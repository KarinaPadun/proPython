# 2 вариант
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
            self.trip_distance += distance
            self.fuel -= distance
            return True
        else:
            print(f"{self.model} не вистачає палива, щоб проїхати {distance} км.")
            return False


car1 = Car("Toyota", "red")
car2 = Car("BMW", "blue")
car3 = Car("Mercedes", "black")

desired_dist = 100
race_dist = 0
while race_dist < desired_dist:
    fuel_empty = True
    for car in [car1, car2, car3]:
        distance = random.randrange(0, 9)
        path = car.move(distance)
        if path:
            race_dist += car.trip_distance
            print(f"{car.color} {car.model} проїхав {distance} км. Загальна відстань: {race_dist} км.")
            if race_dist >= desired_dist:
                print(f"\n{car.color} {car.model} переміг!")
                break
            fuel_empty = False

    if fuel_empty:
        print("Усі машини залишилися без пального. Гонка завершена.")
        break

print(f"{car1.model} проїхав {car1.trip_distance} км, залишилося {car1.fuel} палива.")
print(f"{car2.model} проїхав {car2.trip_distance} км, залишилося {car2.fuel} палива.")
print(f"{car3.model} проїхав {car3.trip_distance} км, залишилося {car3.fuel} палива.")
