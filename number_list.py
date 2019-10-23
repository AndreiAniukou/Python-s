for value in range(0, 10):
    print(value)

numbers = list(range(0, 10, 2))
print(numbers)

sqrs = []
for value in range(0, 10):
    sqr = value**2
    sqrs.append(sqr)
    print(sqrs)

'''LIST GENERATOR'''

sqr = [value**2 for value in range(0, 11)]
print('\n' + str(sqr))