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

n = []
for value in range(0, 21):
    if value % 3 == 0:
        pass
    else:
        value += 1
        n.append(value)
print(n)