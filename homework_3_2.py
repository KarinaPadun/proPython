# черновой вариант
import random

class Car:
    def __init__(self, model, color):
        self.fuel = random.randrange(0, 9)
        self.trip_distance = 0
        self.model = model
        self.color = color

    def move(self, distance):
        if self.fuel > 0:
            # Визначаємо відстань, яку може проїхати автомобіль
            distance_covered = min(self.fuel, distance)
            # Оновлюємо властивості автомобіля
            self.trip_distance += distance_covered
            self.fuel -= distance_covered
            return distance_covered
        else:
            return 0

# Створення екземплярів класу
car1 = Car(model="Toyota", color="Blue")
car2 = Car(model="Honda", color="Red")
car3 = Car(model="Ford", color="Green")

# Налаштування гонки
desired_dist = 50
race_dist = 0

# Цикл гонки
while race_dist < desired_dist:
    # Рух кожного автомобіля
    dist1 = car1.move(random.randrange(0, 9))
    dist2 = car2.move(random.randrange(0, 9))
    dist3 = car3.move(random.randrange(0, 9))

    # Оновлення загальної відстані гонки
    race_dist += max(dist1, dist2, dist3)

    # Перевірка переможця
    if any(car.trip_distance >= desired_dist for car in [car1, car2, car3]):
        winner = next(car for car in [car1, car2, car3] if car.trip_distance >= desired_dist)
        print(f"Автомобіль {winner.color} {winner.model} переміг! Проїхавши {winner.trip_distance} км.")
        break

# Виведення результатів гонки
for car in [car1, car2, car3]:
    print(f"Автомобіль {car.color} {car.model} проїхав {car.trip_distance} км. Запас палива: {car.fuel} л.")
