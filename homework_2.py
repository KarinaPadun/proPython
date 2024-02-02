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
        :param num:
        :return: square number
        """
    return num**2


# 2.2 a
def square(num):
    """
    Функція повертає квадрат числа
    :param num:
    :return: квадрат числа
    """
    return num*num

# 2.3 a

from math import pow


def sqr_number(number):
    """
    Функція приймає число. Метод pow приймає число та зводить його у вказану степінь.
    :param number:
    :return: квадрат числа, float
    """
    return pow(number, 2)

# b Створіть функцію, яка приймає два числа і повертає їхню суму.
# c Створіть функцію яка приймає 2 числа типу int, виконує операцію ділення та повертає чілу частину і залишок.