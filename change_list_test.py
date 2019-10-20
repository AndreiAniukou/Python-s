name = ['Ellie', 'Arsen', ' Max', 'oleg', 'margo', 'ann', 'victoria', 'andre']
inv_el = 'Dear, ' + name[0] + '. I invite u to diner!'
inv_m = 'Dear, ' + name[2] + '. I invite u to diner!'
inv_a = 'Dear, ' + name[-1] + '. I invite u to diner!'
print(inv_el, '\n' + inv_a.title(), '\n' + inv_m)
print(name[2] + " Can't")
del name[2]
name.insert(2, 'Bro')
print(name)
inv_el = 'Dear, ' + name[0] + '. I invite u to diner!'
inv_m = 'Dear, ' + name[2] + '. I invite u to diner!'
inv_a = 'Dear, ' + name[-1] + '. I invite u to diner!'
print('\n' + inv_el, '\n' + inv_a.title(), '\n' + inv_m)

print('\nI have a big table for more peoples')
name.insert(0, 'Tim')
name.insert(5, 'Gloria')
name.append('Geracl')
print(name)
inv_t = 'Dear, ' + name[0] + '. I invite u to diner!'
inv_g = 'Dear, ' + name[5] + '. I invite u to diner!'
inv_q = 'Dear, ' + name[-1] + '. I invite u to diner!'
invite = '\n' + inv_m + '\n' + inv_a + '\n' + inv_el + '\n' + inv_t + '\n' + inv_g + '\n' + inv_q

print(invite)

print('\n___________________')

print('Sry mate, i can invite only two peoples')

non_inv_1 = name.pop(-1)
message = 'Sorry, ' + non_inv_1 + '.' + ' I cant invite u'
print(message.title())

non_inv_2 = name.pop(-2)
message = 'Sorry, ' + non_inv_2 + '.' + ' I cant invite u'
print('\n' + message.title())

non_inv_3 = name.pop(-3)
message = 'Sorry, ' + non_inv_3 + '.' + ' I cant invite u'
print('\n' + message.title())

non_inv_4 = name.pop(-4)
message = 'Sorry, ' + non_inv_4 + '.' + ' I cant invite u'
print('\n' + message.title())

non_inv_5 = name.pop(2)
message = 'Sorry, ' + non_inv_5 + '.' + ' I cant invite u'
print('\n' + message.title())

non_inv_6 = name.pop(0)
message = 'Sorry, ' + non_inv_6 + '.' + ' I cant invite u'
print('\n' + message.title())

non_inv_7 = name.pop(3)
message = 'Sorry, ' + non_inv_7 + '.' + ' I cant invite u'
print('\n' + message.title())

non_inv_8 = name.pop(1)
message = 'Sorry, ' + non_inv_8 + '.' + ' I cant invite u'
print('\n' + message.title())

non_inv_9 = name.pop(1)
message = 'Sorry, ' + non_inv_9 + '.' + ' I cant invite u'
print('\n' + message.title())

del name[0]
del name[0]
print(name)