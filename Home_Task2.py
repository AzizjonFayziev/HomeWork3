# Написать программу которая выводит min из 2 чисел
num = int(input('Enter 1st number:'))
num2 = int(input('Enter 2nd number:'))
large = max(num, num2)
small = min(num, num2)
print(small, large)