user_names = ['CoLT', 'russkiy23', 'svetoslav', 'admin', 'merinda']

main_users = ['admin']

'''
When list is empty

if user_names:
    for user_name in user_names:
        print('Thx for loging in again')
else:
    print('We are need more user!')
'''
for user_name in user_names:
    if user_name in main_users:
        print('Hello ' + user_name + '! Would u like to see a status report?')
    else:
        print('Hello ' + user_name + ', thx for logging in again.')

print('\n______________\nNext test\n__________________\n')

current_users = ['John', 'ellie', 'maX', 'bullet', 'CoLT', 'merida']
new_users = ['maser', 'bf109', 'fw190', 'Bullet', 'colt', 'muserr']

seen = set(map(str.lower, current_users))

for new_user in new_users:
    if new_user.lower() not in seen:
        print('Welcome! ' + new_user)
    else:
        print('Change ur name ' + new_user + '.')

print('\n\n\n')

numbers = [i for i in range(1, 10)]

for number in numbers:
    if number == 1:
        print(str(number) + 'st\n')
    elif number == 2:
        print(str(number) + 'nd\n')
    elif number == 3:
        print(str(number) + 'rd\n')
    else:
        print(str(number) + 'th\n')