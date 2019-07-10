"""Klocki"""

def make_bricks(small, big, goal):

    for x in range(1):
        s = small * 1
        b = big * 5
        g = s + b
        if g >= goal:
            print('OK')
        else:
            print('Nie starczy')

if __name__ == '__main__':
    user_small= int(input('Podaj ilość klocków a:'))
    user_big = int(input('Podaj ilość klocków b:'))
    user_goal = int(input('Podaj długość:'))
    make_bricks(user_small, user_big, user_goal)