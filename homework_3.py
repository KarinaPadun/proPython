import random

class Car:
    def __init__(self, model , color):
        self.model = model
        self.color = color
        self.fuel = random.randrange(0,9)

    def move(self, distance):
        return

car_1 = Car('Mercedes', 'black',  )
car_2 = Car('Audi', 'pink')
car_3 = Car('BMW', 'white')





    while race_dist < desired_dist:


Необхідно написати класс Car який має атрибути fuel(паливо, задається за допомогою random.randrange(0, 9)),
trip_distance(Відстань яку проїхав автомобіль), model (модель авто) та color(колір)
ю реалізувати в класі метод move який приймає distance як аргумент.

Створити 3 екземпляра цього классу

В циклі while race_dist < desired_dist: необхідно для кожного екземпляру класу
викликати метод move та передати йому значення random.randrange(0, 9). Метод
move повинен додавати до trip_distance значення, яке було повернуто методом randomrange та зменшити кількість палива на це ж значення

Як тільки один із автомобілів проїхав відстань більшу або яка дорівнює desired_dist
- вивести повідомлення про те що автомобіль переміг, вказавши марку та дистанцію
яку проїхав цей автомобіль. Цикл необхідно у такому випадку перервати

Після циклу необхідно вивести повідомлення про те скільки і який автомобіль проїхав
, та який у нього запас палива
