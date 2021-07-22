import random

i = 10
while True:
    i += 1
    print(f"{i}========")
    break
print()

print(random.random())
print()

for i in range(5):
    for j in range(i+1):
        print('*', end="")
    print('')

for i in range(5):
    print('{:<5}'.format('*' * (i + 1)))


