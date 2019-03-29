print('{:*^30s}'.format('Задание-1:'))
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    e = 1
    for i in range(ndigits):
        e = 10 * e
    numEnd = (number * e * 10) % 10
    if numEnd>5:
        a1 = (((number * e * 10) // 10) + 1) / e
    elif numEnd<5:
        a1 = ((number * e * 10) // 10) / e
    #I wanna try to make banking round if numEnd = 5...
    else:
        if (number * e) % 2 == 0:
            a1 = ((number * e * 10) // 10) / e
        else:
            a1 = (((number * e * 10) // 10) + 1) / e
    return a1

print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))
print(my_round(2.1234450, 5))

print('{:*^30s}'.format('Задание-2:'))
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    ticket_str = str(ticket_number)
    ticket_list = list(map(int, str(ticket_str)))
    if len(ticket_list) != 6:
        return 'сегодня Удача равнодушна к Вам, но Вы достигните успеха, если сделаете сами маленький шаг вперед'
    elif sum(ticket_list[0:3]) == sum(ticket_list[3:6]):
        return 'Удача обернулась к Вам лицом - ловите момент'
    else:
        return 'Удача не в этом билете. Можете купить новый.'

print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
