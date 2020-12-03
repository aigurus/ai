import random
temps = [[random.randint(10,30) for h in range(24)] for d in range(31)]
#
# the matrix is magically updated here
#
print(temps)
hotDays = 0

for day in temps:
    if day[11] > 20.0:
        hotDays += 1

print(hotDays, "days were hot.")