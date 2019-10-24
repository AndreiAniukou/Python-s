'''
age = int(input('Enter ur age'))

if age <= 4:
    print('ur ticket is free')
elif age <= 18:
    print('ur ticket cost is 5$')
else:
    print('ur ticket cost 10$')
'''

'''
age = int(input('Enter ur age!'))

if age <= 4:
    price = 0
elif age <= 18:
    price = 5
else:
    price = 10

print('Ur ticket cost $' + str(price) + '.')
'''

age = int(input('Enter ur age!'))

if age <= 4:
    price = 0
elif age <= 18:
    price = 5
elif age <= 65:
    price = 10
elif age >= 65:
    price = 5

print('Ur ticket cost $' + str(price) + '.')
