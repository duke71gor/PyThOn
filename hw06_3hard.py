print('{:*^30s}'.format('Задание-1:'))
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки они получают
# удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

# С использованием классов.
# Реализуйте классы сотрудников так, чтобы на вход функции-конструктора
# каждый работник получал строку из файла
import pickle

class Hours_of:
    def __init__(self, Surname, Name, Middlename, work_hrs):
        self.surname = Surname
        self.name = Name
        self.middlename = Middlename
        self.work_hrs = work_hrs

class Workers(Hours_of):
    def __init__(self, Surname, Name, Middlename, salary_norm, work_hrs_norm):
        self.surname = Surname
        self.name = Name
        self.middlename = Middlename
        self.salary_norm = salary_norm
        self.work_hrs_norm = work_hrs_norm
#        self.salary = salary
    def salary(self):
        if (Hours_of.work_hrs / self.work_hrs_norm) > 1:
            return ((Hours_of.work_hrs / self.work_hrs_norm - 1) * 2 + 1) * self.salary_norm
        else:
            return (Hours_of.work_hrs / self.work_hrs_norm) * self.salary_norm

workers = []
f1 = open('data/workers.txt', 'r', encoding='cp1251')
worKers = f1.readlines()
f1.close()

for i in range(1,len(worKers)):
    a = worKers[i].split()
    workers.append([Workers(a[0],a[1],a[2],a[3],a[4])])

hours_of = []
f2 = open('data/hours_of.txt', 'r', encoding='cp1251')
hours_Of = f2.readlines()
f2.close()

for i in range(1,len(hours_Of)):
    a = hours_Of[i].split()
    hours_of.append([Hours_of(a[0],a[1],a[2],a[3])])

for num, workers in enumerate(workers, start=1):
    workers.append(Workers.salary())
    print(workers)