# Задание 1:
# Даны 2 строки:
from random2 import random

first = 'Мама мыла раму'
second = 'Рамена мало было'

# Необходимо составить lambda-функцию для следующего выражения - list(map(?, first, second))
# C помощью функции map и лямбда-функции осуществляется сравнение соответствующих символов двух строк.
# Если символы на одной и той же позиции в строках равны, лямбда-функция возвращает True, в противном случае — False.
print(list(map(lambda x, y: x == y, first, second)))

# Задание 2:
# Функция get_advanced_writer принимает имя файла.
def get_advanced_writer(file_name):
# Внутри неё определена функция write_everything, принимающая любое количество аргументов.
# В write_everything каждый элемент data_set преобразуется в строку и записывается в файл,каждый элемент на новой строке
    def write_everything(*data_set):
        with open(file_name,'a',encoding='utf-8') as f:
            for data in data_set:
                f.write(str(data) + '\n')

    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

# Задание 3:
# Импортируем функцию choice из модуля random, которая используется для случайного выбора элемента из последовательности
from random import choice
# Создается класс MysticBall
class MysticBall:
#  Метод __init__принимает произвольное количество аргументов (*words), которые затем сохраняются как атрибут self.words
    def __init__(self,*words):
        self.words=words
#  Метод call выбирает случайный элемент из списка self.words с помощью функции choice.
#  Этот метод будет возвращать один из вариантов ответа.
    def __call__(self):
        return choice(self.words)
# Создается объект first_ball класса MysticBall, передаются три слова в конструктор.
first_ball = MysticBall('Да', 'Нет', 'Наверное')

print(first_ball())
print(first_ball())
print(first_ball())
