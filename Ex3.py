#Задача 3:Напишите программу, которая на вход принимает
#5 чисел и находит максимальное из них.

print('Введите числа')
numbers = [int(i) for i in input ().split()]
print (max(numbers))
print (min(numbers))

# Решене 2
# a = list(map(int,input().split()))
# maxvalue = max(a)
# print (maxvalue)