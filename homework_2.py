# 1 Рядки (Strings):
# a Напишіть функцію, яка приймає рядок і повертає його довжину.
# b Створіть функцію, яка приймає два рядки і повертає об'єднаний рядок.

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
    додається +1 до рахунку. Рахунок дорівнює довжині строки


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

    :param string_1:
    :return:
    """
    return sum(map(lambda x: 1, string_1))


# 2 Числа (Int/float):
# a Реалізуйте функцію, яка приймає число і повертає його квадрат.
# b Створіть функцію, яка приймає два числа і повертає їхню суму.
# c Створіть функцію яка приймає 2 числа типу int, виконує операцію ділення та повертає чілу частину і залишок.