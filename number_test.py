"""num = list(range(0,21))
print(num)

print('\n\n________________________\n')

# one million

mill = []
for value in range(0, 1000001):
    mill.append(value)
print(mill)
print(len(mill))

#Min max sum

print('\n' + str(min(mill)))
print(max(mill))
print(sum(mill))
"""
#odd number

n = list(range(1, 20, 2))
print(n)

print('\n\n_________\n')

n = list(range(3, 30, 3))
print(str(n) + '\n')
 # ^3
n = []
for value in range(1, 10):
    s = value ** 3
    n.append(s)
print(str(n) +'\n')

# Generator

cube = [value ** 3 for value in range(1, 30)]
print(cube)
