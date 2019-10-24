name_players = ['mark', 'martina', 'andre', 'elli', 'john', 'edgar']
print(name_players[0:3]) #Only first 3 name
print(name_players[:3]) #without first index python start in first element list
print(name_players[2:])
print(str(name_players[-3:]) + '\n') #last 3 players

print('My team: ')
for player in name_players[3:]:
    print(player.title())
print('\n\n\n')

#Copy list

my_foods = ['pizza', 'marshmallow', 'shawerma', 'chips', 'draniki']
friend_food = my_foods[:]

print('My favorite foods: ')
print(my_foods)

print('\nMy friend food: ')
print(str(friend_food) + '\n')

my_foods.append('ice cream')
friend_food.append('cola')
print(my_foods)
print(friend_food)
print('\n\n_____________\n')

'''Doesn't work copy'''

friend_food = my_foods

my_foods.append('zefir')
friend_food.append('sprite')
print(my_foods)
print(friend_food)