from os.path import exists
from file_writing import writing_scv, writing_txt, get_info
from export import from_file



def choice():
    while True:
        print('\nМЕНЮ')
        print("--------------------------------------")
        print('1. Показать все записи.')
        print('2. Добавить новую запись в базу CSV')
        print('3. Добавить новую запись в базу TXT')
        print('4. Закрыть программу.')
        print("--------------------------------------")
        n = сhecking_the_number(input('Выберите пункт меню: '))

        if n == 1:
            
            print('Телефонная книга в формате  CSV')
            print("--------------------------------------")
            print(from_file('Phonebook.csv'))
            print("--------------------------------------")
            print('\n\nТелефонная книга в формате  TXT')
            print("--------------------------------------")
            print(from_file('Phonebook.txt'))
            print("--------------------------------------")
            

        elif n == 2:
            info = get_info()
            writing_scv(info)
        
        elif n == 3:
            info = get_info()
            writing_txt(info)
     
        elif n == 4:
          
            print('Спасибо за работу!')
            break

        else:
            print(
                '\nТакого пункта меню не существует.\nВведите цифру, соответствующую пункту меню.')


def сhecking_the_number(arg):
    while arg.isdigit() != True:
        print('\nВы ввели не число.')
        arg = input('Введите соответствующий пункт меню: ')
    return int(arg)

    