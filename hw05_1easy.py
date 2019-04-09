import sys, os, time

def makeDir():
    dir_name = input('Введите имя новой дирректории \n:')
    try:
        os.mkdir(os.path.join(os.getcwd(), dir_name))
        print(f'{dir_name} успешно создана')
        time.sleep(4.0)
    except FileExistsError:
        print(f'невозможно создать {dir_name}')
        time.sleep(4.0)

def removeDir():
    dir_name = input('Введите имя дирректории под снос \n:')
    try:
        os.rmdir(dir_name)
        print(f'{dir_name} успешно удалена')
        time.sleep(4.0)
    except FileNotFoundError:
        print(f'невозможно удалить {dir_name}')
        time.sleep(4.0)

print('{:*^30s}'.format('Задание-1:'))
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

#creation:
for i in range(1,10):
    try:
       os.mkdir(os.path.join(os.getcwd(), f'dir_{i}'))
    except FileExistsError:
        print('Такая дирретория уже существует')

#delete:
answ = input('удалить? (Y/N) \n:')
if answ == 'Y':
    for i in range(1,10):
        try:
            os.rmdir(f'dir_{i}')
        except FileNotFoundError:
            print('Такая дирректория не существует')
else:
    exit()


print('{:*^30s}'.format('Задание-2:'))
# Напишите скрипт, отображающий папки текущей директории.
import os

for i in os.listdir(): print(i)



print('{:*^30s}'.format('Задание-3:'))
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
import os
import sys

os.system(f'copy {os.path.basename(sys.argv[0])} Копия_{os.path.basename(sys.argv[0])}')

