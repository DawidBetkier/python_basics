"""Problem Collatza"""

def Collatz (number):
    """Policzenie problemu"""

    print(number)

    if number == 1:
        return #zwraca printa i koniec
    elif number % 2 != 0:
        return Collatz(number * 3 + 1)
    else:
        return Collatz(number//2)

if __name__ == '__main__':
    num = int(input('Podaj liczbę początkową: '))
    Collatz(num)