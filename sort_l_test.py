

travel = ['USA', 'France', 'Egyrt', 'Russia', 'Spain', 'China', 'Argentina', 'Belarus']
print('\nOriginal list: ' + str(travel))

print('\nSorted list: ' + str(sorted(travel)))

print('\nOriginal: ' + str(travel))

print('\nReverse: ' + str(sorted(travel, reverse=True)))

print('\nOriginal 2: ' + str(travel))

print('\n__________________\n')

travel.reverse()
print('\nOriginal revers: ' + str(travel))

travel.reverse()
print('\nOriginal back: ' + str(travel))

travel.sort()
print('\nOriginal sort: ' + str(travel))

travel.sort(reverse=True)
print('\nOriginal sort revers: ' + str(travel))

'''FROM change_lsit_test i cope 'name' list'''

name = ['Ellie', 'Arsen', ' Max', 'oleg', 'margo', 'ann', 'victoria', 'andre']

print('\n' + str(len(name)))

'''TEST PROGRAMM WITH ALL FUN LIST'''

print('\n__________________')

car_name = ['audi', 'aston martin', 'bmw', 'mercedes', 'toyota', 'gmc',
            'maybah', 'vw', 'volvo', 'maserati', 'kia', 'honda', 'nissan']
print(car_name)

car_name.sort()
print('\n' + str(car_name))

car_name.sort(reverse=True)
print(car_name)

print(sorted(car_name))
print(sorted(car_name, reverse=True))

car_name.reverse()
print(car_name)