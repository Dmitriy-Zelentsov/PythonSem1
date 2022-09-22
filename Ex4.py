#Задача 4: Напишите программу, которая будет принимать число N
# и будет выводить числа оот -N до N

number = int(input ())
i = -number
while i <=number:
    print(i)
    i += 1

# Решение2

n = int(input())
mass = []
for i in range(-n,n+1,1):
    mass.append(i)
print(mass)



