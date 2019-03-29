print('{:*^30s}'.format('Задание-1:'))
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3

inpNum = input('Введите дроби, котрые Вы желате сложить или вычесть в виде: n x/y +- n x/y \n:')

inpNumSp = inpNum.split('+')
if len(inpNumSp) < 2:
    inpNumSp = inpNum.split(' - ')

inpFr1 = inpNumSp[0]
inpFr2 = inpNumSp[1]

#для 1ой дроби: (1-1-целая часть(a1), 1-2-числитель(b1), 1-3знаменатель(c1))
def bcFr(inpFr):
    inpFr1_3 = inpFr.split('/')
    if len(inpFr1_3) == 2:
        c = int(inpFr1_3[1])
    else:
        c = 1
    inpFr1_2 = inpFr1_3[0].split()
    if len(inpFr1_2) == 2:
        a = int(inpFr1_2[0])
        b = int(inpFr1_2[1])
        b = a * c + b
    else:
        b = int(inpFr1_2[0])
    return [b, c]

bc1 = bcFr(inpFr1)
b1 = int(bc1[0])
c1 = int(bc1[1])
bc2 = bcFr(inpFr2)
b2 = int(bc2[0])
c2 = int(bc2[1])
res_c = c1 * c2

for i in range(len(inpNum)):
    if inpNum[i] == '+':
        res_b = (b1 * c2 + b2 * c1)
        break
    else:
        res_b = (b1 * c2 - b2 * c1)

print(res_b//res_c,'',res_b%res_c,'/',res_c)



print('{:*^30s}'.format('Задание-2:'))
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"
import os
import pickle

DIR = 'data'
oKlad = 2400 #оклад при 184 часов работы в месяц
workNorm = 184 #часов в месяц по норме
idNum = [125546,234594,346859,4485960,5507847,604849,7895610,1145670,13604914,15559316,17964418,19593320] #id-numbers для рабочих
for i in range(len(idNum)): #цикл прохождения по всем id-numbers рабочих
    wanted_symbol = idNum[i]
    with open(os.path.join(DIR, 'hours_of'), 'r', encoding='UTF-8') as f:
        for line in f:  # считываем файл построчно
            if wanted_symbol in line:  # пока не найдем нужную информацию
                lineList = line.split() #разделяем линию на список
                workHrs = int(lineList[-1])#берем последний элемент - отработанные часы и переводим в int
                if workHrs > workNorm:
                    salary = ((workHrs/workNorm - 1) * 2 + 1) * oKlad
                else:
                    salary = (workHrs/workNorm ) * oKlad
                with open(os.path.join(DIR, 'workers'), 'a', encoding='UTF-8') as f:
                    'workers'.write('Зарплата рабочего с id {} равна {}'.format(wanted_symbol, salary))



print('{:*^30s}'.format('Задание-3:'))
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))

DIR = 'data'

with open(os.path.join(DIR, 'fruits'), 'r', encoding='UTF-8') as f:
    f.read()
    ordList = (list(map(chr, range(ord('А'), ord('Я') + 1))))

for chr in range(ord('A'), ord('Я')):
    nametext = ('fruits_'.chr)
fileWrite(nametext, w, map(chr, range(ord('A'))))


def fileWrite(nametxt, w, firstline):
    file = open(nametxt, w)
    file.write('firstline \n')
    file.close()

