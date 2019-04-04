import os, time, sys

#функции создания новой дирректории и ее удаления для hw05_normal:
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

def changeDir():
    print('You are here:')
    dir_1 = os.getcwd()
    print('your current dir: ', os.getcwd())
    # Use '\\' while changing the directory
    dir_new = input('Введите конечную папку перехода:')
    if dir_new == '':
        print('не введена какая-либо дерретория')
        time.sleep(4.0)
        return
    os.chdir(dir_new)
    print('your new dir:', os.getcwd())
    time.sleep(8.0)
    dir_2 = os.getcwd()
    if dir_1 == dir_2:
        print('Переход неудачный, попробуйте снова')
        time.sleep(4.0)
    else:
        print('Вы прибыли по месту назначения...')
        time.sleep(4.0)

def file_copy():
    print('В вашей дирреткории есть такие папки и файлы:', os.listdir())
    file_name = input('Наберите файл для копирования \n:')
    try:
        os.system(f'copy {file_name} Копия_{file_name}')
        print(f'Копия_{file_name} успешно созданa')
        time.sleep(4.0)
    except FileExistsError:
        print(f'невозможно создать {file_name}')
        time.sleep(4.0)

def removeFile():
    print('В вашей дирреткории есть такие папки и файлы:', os.listdir())
    filename = input('Введите имя файла для удаления \n:')
    answ = input('Последний шанс: удалить или оставить? [Y] - если удалить, [ENTER] - если оставить \n:')
    if answ == 'Y':
        try:
            os.remove(filename)
            print(f'файл {filename} успешно удален')
            time.sleep(4.0)
        except OSError:
            print(f'Что-то пошло не так и файл: {filename} остался, попробуйте сперва закрыть файл')
            time.sleep(4.0)
    else:
        return

def dir_Path():
    print(os.path.dirname(os.path.realpath(__file__)))
    time.sleep(6.0)

