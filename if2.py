req_top = ['mushrooms', 'green paper', 'extra cheese']

for req_tops in req_top:
    if req_tops == 'green paper':
        print('we are out gp right now')
    else:
        print('Addig ' + req_tops + '.')

print('\nFinish\n__________________\n')

# _____________________________________

requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print('Adding ' + requested_topping + '.')
    print('Finish pizza')
else:
    print('Sure?')


print('\n\n\n_______________________________\n')

available_toppings = ['mushrooms', 'olives', 'green paper', 'pepperoni',
                      'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print('Adding ' + requested_topping + '.')
    else:
        print('Sorry, we dont have adding ' + requested_topping + ' in pizza.')

print('finish!')
