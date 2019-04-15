#!/Ihor Piriyenko/bin/python3

"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87      
      16 49    55 77    88    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html

"""
import random
import time

def cart():
    cart = drum.copy() # Формируем новый список для карточек.. из списка случайных бочонков
    random.shuffle(cart) # Перемешиваем
    cart = cart[0:15] # Берем первых пятнадцать уникальных номеров
    cart.sort() #Сортируем их по возрастанию
    a = [0, 1, 2]
    random.shuffle(a) #формируем случайное начало выборки чисел из сart
    cart1 = cart[a[0]::3]#line-1
    [cart1.insert(random.randint(0, len(cart1)), ' ') for x in range(4)]#заполняем line-1 4-мя пробелами в случайном порядке
    cart2 = cart[a[1]::3]#line-2
    [cart2.insert(random.randint(0, len(cart2)), ' ') for x in range(4)]#заполняем line-2 4-мя пробелами в случайном порядке
    cart3 = cart[a[2]::3]#line-3
    [cart3.insert(random.randint(0, len(cart3)), ' ') for x in range(4)]#заполняем line-3 4-мя пробелами в случайном порядке
    cart_lst = cart1 + cart2 + cart3
    return cart_lst

def showCard(lst): #вывод одной карты на экран
    print(' '.join(map(str, lst[0:9])))
    print(' '.join(map(str, lst[9:18])))
    print(' '.join(map(str, lst[18:27])))
    print('-----------------------')

def firstStep(lst1, lst2): #Вывод двух карт на экран
    print('--Карточка компьютера--')
    showCard(lst1)
    print('-----Ваша карточка-----')
    showCard(lst2)

def checkRemove(lst, x): #Проверяем карту на наличие числа Х и зачеркиваем его
    for id, item in enumerate(lst):
        if item == x:
            lst[id] = '-'
            return lst

def checkCart(lst, x): #Проверяем карту на наличие числа Х и если есть --> True
    for item in (lst):
        if item == x:
            return True

def compareCart(): #Сравнение двух карт на наличие незачеркнутых чисел
    cart_strPC = (' '.join(map(str, cart_lstPC)))
    cart_strG = (' '.join(map(str, cart_lstG)))
    if cart_strPC.isdigit() == True and cart_strG.isdigit() == True:
        return 111 #Ничья
    if cart_strPC.isdigit() == True and cart_strG.isdigit() == False:
        return 110 #Gamer lost
    if cart_strPC.isdigit() == False and cart_strG.isdigit() == True:
        return 101 #Gamer win

# Список от 1 до 90 в возрастающей последовательности
drum_Zero = []
for i in range(1, 91):
    drum_Zero.append(i)

while True:
    answQ = input('Если хотите выйти - нажмите [q]/[Q], или иную другую, если хотите продолжить \n:')
    if answQ == 'q' or answQ == 'Q':
        break
    else:
        drum = drum_Zero.copy()
        random.shuffle(drum) # Перемешиваем список случайных боченков в drum
        cart_lstPC = cart() #Карта компьютера
        cart_lstG = cart()  #Карта геймера
        for i in range(len(drum)):
            print('Бочонок №: ', drum[i])
            firstStep(cart_lstPC, cart_lstG) #Вывод двух карт: PC & gamer
            answ = input('Желаете зачеркнуть цифру {} на вашей краточке? Если да, нажмите [y]/[Y]\n:'.format(drum[i]))
            if answ == 'y' or answ == 'Y':
                if checkCart(cart_lstG, drum[i]) == True:
                    [checkRemove(cart_lstG, drum[i])]
                else:
                    print('--==GAME OVER==--')
                    print(f'У Вас не было цифры: {drum[i]}, но Вы ее хотели зачеркнуть')
                    time.sleep(6.0)
                    break
            else:
                [checkRemove(cart_lstPC, drum[i])]
                if checkCart(cart_lstG, drum[i]) == True:
                    print('--==GAME OVER==--')
                    print(f'У Вас была цифра: {drum[i]}, но Вы ее пропустили')
                    time.sleep(6.0)
                    break
                # Сравнение двух карт на отсутствие незачеркнутых чисел
                elif compareCart() == 111:
                    print('--==НИЧЬЯ==--')
                    time.sleep(6.0)
                    break
                elif compareCart() == 110:
                    print('--==Вы проиграли==--')
                    time.sleep(6.0)
                    break
                elif compareCart() == 101:
                    print('--==ВЫ ПОБЕДИЛИ==--')
                    time.sleep(6.0)
                    break
                else:
                    pass
