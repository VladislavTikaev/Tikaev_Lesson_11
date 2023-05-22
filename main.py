# Задача №1
import random

Matrix = [[0]*5 for i in range(5)]
for i in range(5):
 for j in range(5):
  Matrix[i][j] = random.randint(-20,20)
  print(Matrix[i][j], end='\t')
 print()

my_sum = 0
for i in Matrix:
 if sum(i) > my_sum: my_sum=sum(i)
print(my_sum)

max_el = 0
for i in range(5):
 if Matrix[i][i]>max_el: max_el = Matrix[i][i]
print(max_el)

count = 0
for i in range(5):
 for j in range(5):
  if Matrix[i][j]<0 and j<i: count += 1
print(count)
# Задача №2
# Ввод с клавиатуры. Если строка введённая с клавиатуры – это числа, то поделить первое на второе. Обработать ошибку деления на ноль. Если второе число 0, то программа запрашивает ввод чисел заново. Также если были введены буквы, то обработать исключение.
# Обработать исключения на TypeError и ValueError

while True:
 try:
  number_1 = int(input('Введите первое число: '))
  number_2 = int(input('Введите второе число: '))
  c = number_1/number_2
 except TypeError:
  print('Введен неверный тип данных')
 except ValueError:
  print('Аргумент некорректного значения')
 except ZeroDivisionError:
  print('На ноль делить нельзя!')
 else:
  print(c)
  break
