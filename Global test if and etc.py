

bad_password = ['qwerty123', '1234', 'zxcvb', 'user']


users = list(input('Enter ur login'))
users_password = list(input('Enter ur password'))

while True:
    if users in users:
      print('change ur name')

    if users_password == bad_password:
      print('Ur password very bad')

