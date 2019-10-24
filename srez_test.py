my_foods = ['pizza', 'marshmallow', 'shawerma', 'chips', 'draniki']
print('The first three items in the list are:')
print(my_foods[:3])
print('\nThe items from he middle of the list area:')
print(my_foods[2:4])
print('\nThe last three:')
print(my_foods[2:])

print('\n\n__________\n')

pizza = ['peperoni', 'margarita', '4 season', 'hum and mushrooms']
friend_pizza = pizza[:]
pizza.append('tut.by')
friend_pizza.append('silicia')
print('My pizza:')
print(pizza)
print('\nFriends pizza:')
print(friend_pizza)

print('\n\nMy pizza:')
for name_pizza in pizza:
    print(name_pizza)

print('\nFriends pizza')
for fr_pzz in friend_pizza:
    print(fr_pzz)


car = ['bmw', 'volvo', 'audi', 'mercedes', 'koeneggsegg']
print('\nI have a car:')
for cn in car:
    print(cn.title())