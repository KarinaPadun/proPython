# 1 Рядки (Strings):
# a Напишіть функцію, яка приймає рядок і повертає його довжину.

# 1.1 a
a = '123456'
print(len(a))

# 1.2 a


def length_string(string):
    """
    returns the length of the string

    """
    return len(string)

# 1.3 a


def length(string):
    """
    Функція перебирає елементи строки. З кожним елементом
    додається +1 до рахунку. Рахунок дорівнює довжині строки.


    :param string:
    :return: length string
    """
    counter = 0
    for _ in string:
        counter += 1
    return counter


# 1.4 a

def length_map(string_1):
    """
    Функція приймає строку та віддає кількість елементів строки.
    Анонімна функція присвоює 1 елементу, функція map
    застосовує анонімну функцію до кожного елементу строки.

    :param string_1:
    :return:length string
    """
    return sum(map(lambda x: 1, string_1))

# 1.1 b  Створіть функцію, яка приймає два рядки і повертає об'єднаний рядок.


def string(string_1, string_2):
    fin_string = string_1 + string_2
    return fin_string
    # return string_1 +string_2

# 1.2 b


def final_string(string_1, string_2):
    """
    Повертає об'єднанну строку

    :param string_1:
    :param string_2:
    :return: concatenated string
    """
    result = ''.join([string_1, string_2])
    return result


# 1.3 b
def final_str_f(str1, str2):
    fin_str = f"{str1}{str2}"
    return fin_str


# 2 Числа (Int/float):
# a Реалізуйте функцію, яка приймає число і повертає його квадрат.

# 2.1 a

def square_num(num):
    """
        Function return square number
        :param num: int
        :return: square number , float
        """
    return num**2


# 2.2 a
def square(num):
    """
    Функція повертає квадрат числа
    :param num: int
    :return: квадрат числа, float
    """
    return num*num

# 2.3 a

from math import pow


def sqr_number(number):
    """
    Функція приймає число. Метод pow зводить число у вказану степінь.
    :param number: int
    :return: квадрат числа, float
    """
    return pow(number, 2)


# 2.1 b Створіть функцію, яка приймає два числа і повертає їхню суму.

def sum_numbers(number_1, number_2):
    """
    Return sum numbers

    :param number_1: int, float
    :param number_2: int, float
    :return: sum , float
    """
    return sum([number_1, number_2])

# 2.2 b


def summ(num_1, num_2):
    """
    Return sum numbers

    :param num_1:
    :param num_2:
    :return: sum
    """
    return num_1 + num_2

# 2.1 c Створіть функцію яка приймає 2 числа типу int, виконує операцію ділення та повертає чілу частину і залишок.


def division(number_1, number_2):
    """
    Функція приймає два числа , виконує цілочисленне ділення та обчислює залишок від ділення

    :param number_1:   int
    :param number_2: int
    :return: цілу частину та залишок від ділення
    """
    return number_1 // number_2, number_1 % number_2

# 3.1 Списки (Lists):
# a Напишіть функцію для обчислення середнього значення списку чисел.


def average_value(list_1):
    """
    Повертає середнє значення списку, ділячи сумму чисел на їх кількість

    :param list_1:
    :return: average value list, float
    """
    return sum(list_1) / len(list_1)

# 3.2 a
import statistics


def average_val(list_2):
    """
    Приймає список чисел. Повертає середне значення списку за допомогою методу statistics.mean

    :param list_2:
    :return: середне значення списку
    """
    return statistics.mean(list_2)


# 3.1 b Реалізуйте функцію, яка приймає два списки і повертає список, який містить спільні елементи обох списків

def unique_symbols(list1, list2):
    """
    Функція приймає два списка та перевіряє входження кожного елементу.
    Якщо елемент є в обох списках, то він додається в список спільних елементів

    :param list1:
    :param list2:
    :return: список спільних елементів списків
    """
    list3 = [i for i in list1 if i in list2]
    return list3


