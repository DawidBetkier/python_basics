digit_to_area = {
    0: 'Warszawa',
    1: 'Olsztyn',
    2: 'Lublin',
    3: 'Kraków',
    4: 'Katowice',
    5: 'Wrocław',
    6: 'Poznań',
    7: 'Szczecin',
    8: 'Gdańsk',
    9: 'Łódź',
}

def get_city(zip_code):
    if len(zip_code) !=6:
        return None
    if zip_code[2] != '-':
        return None
    if not (zip_code[:2] + zip_code[3:]).isdigit():
        return None
    return digit_to_area[int(zip_code[0])]

if __name__ == '__main__':
    code = input('Podaj swój kod pocztowy: ')
    city = get_city(code)

    if city:
        print(f'Wiatj gościu z miasta {city}')
    else:
        print('Nieprawidłowy kod pocztowy!')
