"""Wyznaczanie liczb parzystych"""

def parzyste(number):
    for i in range(number):
        if number % 2 == 0:
            print(number)
            number -= 1
        else:
            number -= 1

if __name__ == '__main__':
    user_num = int(input('Podaj liczbę startową: '))
    parzyste(user_num)
    print(f'Oto liczby parzyste od {user_num} do 0')



