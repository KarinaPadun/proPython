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

def common_elements(list1, list2):
    """
    Функція приймає два списка та перевіряє входження кожного елементу.
    Якщо елемент є в обох списках, то він додається в список спільних елементів

    :param list1:
    :param list2:
    :return: список спільних елементів списків
    """
    list3 = [i for i in list1 if i in list2]
    return list3

# 3.2 b


def new_list(list1, list2):
    """
       Функція приймає два списка та повертає список спільних елементів

       :param list1:
       :param list2:
       :return: список спільних елементів списків
       """
    return list(set(list1) & set(list2))


# 3.3 b
def common_element(list1, list2):
    """
    Функція приймає два списки та повертає ліст спільних унікальних елементів списків
    :param list1:
    :param list2:
    :return: list common elements
    """
    return list(set.intersection(set(list1), set(list2)))

# 4.1 Словники (Dictionaries):
# a Створіть функцію, яка приймає словник і виводить всі ключі цього словника.


def keys_dict(dict_1):
    """
    Функція для виведення всіх ключів словника

    :param dict_1:
    :return: keys dict
    """
    return dict_1.keys()

# 4.2 a


def keys_dictionary(dict_2):
    """
    Функція приймає словник та повертає ключі цього словника
    :param dict_2:
    :return: список ключів словника
    """
    return list(key for key in dict_2)


# 4.1 b Реалізуйте функцію, яка приймає два словники і повертає новий словник, який є об'єднанням обох словників.


def new_dict(dict1, dict2):
    """
    Функція приймає два словника. Створюємо копію словника 1 ,щоб поверталось значення замість None.
    Додаємо елементи другого словника до першого

    :param dict1:
    :param dict2:
    :return: об'єднанний словник
    """
    dict_3 = dict1.copy()
    dict_3.update(dict2)
    return dict_3


# 4.2 b
def new_dict_1(dict1, dict2):
    """
    Функція приймає два словника та повертає новий об'єднанний словник

    :param dict1:
    :param dict2:
    :return: новий об'єднанний словник
    """
    return new_dict(dict1, dict2)


# 5.1 Множини (Sets):
# a Напишіть функцію, яка приймає дві множини і повертає їхнє об'єднання.

def union_set(set_1, set_2):
    """
    Функція приймає множини та повертає іх об'єднання

    :param set_1:
    :param set_2:
    :return: повертає їхнє об'єднання
    """
    return set_1.union(set_2)

# 5.2 а


def union_of_sets(set1, set2):
    """
    Функція об'єднання двох множин
    :param set1:
    :param set2:
    :return: Об'єднання множин
    """
    return set1 | set2


# 5.3 а

# 5.1 b Створіть функцію, яка перевіряє, чи є одна множина підмножиною іншої.

A = {1, 2}
B = {4, 5}
print(A | B)


# 6.1 Умовні вирази та цикли:
# a Реалізуйте функцію, яка приймає число і виводить "Парне", якщо число парне, і "Непарне", якщо непарне.

def pair_number(num):
    """
    Функція, яка визначає, чи є число парним чи непарним

    :param num: Число
    :return: Рядок "Парне" або "Непарне"
    """
    if num % 2 == 0:
        return 'Парне'
    else:
        return 'Непарне'

# 6.2 a


def pair_num(number):
    """
    Функція, яка визначає, чи є число парним чи непарним

    :param number:
    :return:  "Парне" або "Непарне"
    """
    return 'Парне' if not number % 2 else 'Непарне'

# 6.3 a


def pair_numb(number):
    """
    Функція, яка визначає, чи є число парним чи непарним

    :param number:
    :return:  "Парне" або "Непарне"
    """
    answer = ['Непарне', 'Парне']
    return answer[int(number % 2 == 0)]

# 6.1 b Створіть функцію, яка приймає список чисел і повертає новий список, що містить тільки парні числа.


def pair_number_list(list_1):
    """
    Function return pair numbers list
    :param list_1:
    :return: pair_number_list
    """
    new_list = []
    for i in list_1:
        if i % 2 == 0:
            new_list.append(i)
    return new_list

# 6.2 b

# 6.3 b




list_1 = [1,2,3,4,5,6]

new_list = []

for i in list_1:
    if i % 2 == 0:
        new_list.append(i)
print(new_list)