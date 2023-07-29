# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. 

from random import randint

set_1 = [randint(-5, 5) for i in range(int(input("Введите кол-во элементов 1-го множества: ")))]
set_1 = set(set_1)
print(set_1)

set_2 = [randint(-5, 5) for i in range(int(input("Введите кол-во элементов 2-го множества: ")))]
set_2 = set(set_2)
print(set_2)

print(sorted(set_1.intersection(set_2)))
