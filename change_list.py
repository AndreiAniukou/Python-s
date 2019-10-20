moto = ['honda', 'yamaha', 'suzuki']
print(moto)

moto[0] = 'ducati'
print('\n' + str(moto))

moto.append('bmw') # Add new element in end list
print(moto)

moto = []
moto.append('bmw')
moto.append('honda')
moto.append('suzuki')
print(str(moto) + ' Append')

moto.insert(2, 'ducati')
print(str(moto) + ' INSERT')

moto = moto
print(moto)

del moto[0] #Delete one element in list if u know it number
print('\n' + str(moto) + ' DELETE')


print(str(moto) + ' POP')

pop_moto = moto.pop()
print(moto)
print(pop_moto)

motor = ['honda', 'suzuki', ' bmw']
first_moto = motor.pop(1)
print('\n\t' + 'My first bike was ' + first_moto + '.')

print('\n' + 'REMOVE')

motor = ['honda', 'bmw', 'ducati', 'yamaha']
print(motor)

motor.remove('ducati')
print(motor)

too_expensive = 'bmw'
motor.remove(too_expensive)
print('\nA ' + too_expensive.title() + ' too expensive')