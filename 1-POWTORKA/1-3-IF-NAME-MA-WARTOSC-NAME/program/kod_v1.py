import time


def calculate_average_bat_lifespan(temp):
    return 4


print(
    'Witaj w programie do wyliczania średniej długości życia'
    'Gacka brunatnego na podstawie średniej temperatury w Aregentynie'
    'w latach 1989-1993'
)

avg_temp = input(
    'Podaj średnią wartość temeratur w Argentynie w latach 1989-1993: ')

print('Obliczam średnią długość życia gacka...')

time.sleep(10)

avg_lifespan = calculate_average_bat_lifespan(avg_temp)

print(f'Średnia długość życia gacka brunatnego wynosi: {avg_lifespan} lat/a')
