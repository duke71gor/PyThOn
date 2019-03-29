print('{:*^30s}'.format('Задание-1:'))
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    fib1 = fib2 = 1
    if m < 2:
        print('Первых два элемента ряда Фибоначчи: 1, 1. \nm - должно быть не меньше двух')
    elif m < n:
        print('n должна быть меньше m')
    if n == 1:
            print(fib1, end=' ')
    elif n == 2:
            print(fib2, end=' ')
    for i in range(2, m):
        fib1, fib2 = fib2, fib1 + fib2
        if m >= n:
            print(fib2, end=' ')

print('{:*^30s}'.format('Задание-2:'))
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

def sort_to_max(origin_list):
    N = len(origin_list)
    for n in range(N-1): #цикл повторения пузырькового сравнения для следующего прохода оставшихся элементов
        for i in range(N-1-n): #цикл сравнения для одного элемента, чтобы найти МАХ и переместить его вправо
            if origin_list[i] > origin_list[i + 1]:
                origin_list[i], origin_list[i + 1] = origin_list[i + 1], origin_list[i]
    print(origin_list)

sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])

print('{:*^30s}'.format('Задание-3:'))
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.
def myFilter(func, iterator):
    iterator = list(iterator) #change tuple or string 2 list
    iterator = list(map(int, list(iterator))) #change list's elements 2 integer
    iterator2 = []
    for i in range(len(iterator)):
        iterator2.append((func)(iterator[i]))
    return iterator2

a = '0123456'
print('a = "0123456"')
print('3x Multiplicate:', myFilter(lambda x: x * 3, a))

print('{:*^30s}'.format('Задание-4:'))
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.
A1 = [20, 20]
A2 = [30, 50]
A3 = [80, 20]
A4 = [90, 50]
print('Например: \nA1=', A1, '\nA2=', A2, '\nA3=', A3, '\nA4=', A4)
xy = list(zip(A1, A2, A3, A4))
x = list(xy[0])
y = list(xy[1])
x.sort()
y.sort()
# (y=y - parallel base lines)      && (deltaX=const) - para--gramm
if y[0] == y [1] and y[2] == y[3] and (x[1] - x[0] == (x[3] - x[2])):
    print("Это параллелограмм")
