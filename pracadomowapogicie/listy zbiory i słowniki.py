"""Operacje na listach, zbiorach i słownikach"""

my_list = [1, 2, 'rysik', 10, 4.65, ]
my_set = {1, 2, 3, 1, 5, 1, 2, }
my_book = {'policja':997, 'straż_pożarna':998, 'pogotowie':999}

def lista(lista):
    print(lista)
    lista.append('dodane')
    print(lista)
    lista.pop()
    print(lista)
    lista.remove('rysik')
    print(lista)
    lista.sort()
    print(lista)
    lista.reverse()
    print(lista)
def zbior(user_set):
    print(user_set)
    user_set.difference()
    print(user_set.difference())



if __name__ == '__main__':
    lista(my_list)
    zbior(my_set)
