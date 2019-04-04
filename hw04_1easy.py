# Все задачи текущего блока решите с помощью генераторов списков!

print('{:*^30s}'.format('Задание-1:'))
# Дан список, заполненный произвольными целыми числами. 
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

res = [x ** 2 for x in [1, 2, 4, 0]]
print(res)

print('{:*^30s}'.format('Задание-2:'))
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.


lst1 = ['fruit1', 'fruit12', 'fruit21', 'fruit13', 'fruit31', 'fruit41', 'fruit14', 'fruit15', 'fruit51']
lst2 = ['fruit13', 'fruit36', 'fruit46', 'fruit14', 'fruit15', 'fruit56', 'fruit61', 'fruit12', 'fruit61']
print('E.g: we have 1st list of fruites \n:', lst1)
print('and we have 2nd list of fruites \n:', lst2)
print('Получить список фруктов, присутствующих в обоих исходных списках:')

res = [lst1[i] for i in range(len(lst1)) for n in range(len(lst2)) if lst1[i] == lst2[n]]
print(res)

print('{:*^30s}'.format('Задание-3:'))
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

import random

#random lst
lst = [random.randint(-99, 99) for _ in range(21)]
print('This is random list: from -99 till +99, with 21 elements \n:', lst)
print('''Получаем список из элементов исходного, удовлетворяющих следующим условиям:
+ Элемент кратен 3
+ Элемент положительный
+ Элемент не кратен 4''')
res = [el for el in lst if el % 3 == 0 and el >= 0 and el % 4 != 0]
print(res)