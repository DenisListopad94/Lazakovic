#Задача1
#a = int(input("Введите перове число: "))
#b = int(input("Введите второе число: "))
#c = int(input("Введите третье число: "))
#print(a < 0 or b < 0 or c < 0)

#Задача2
#n = int(input("n: "))
#k = int(input("k: "))
#print(n % 2 == k % 2)

#Задача3
#a = int(input("a: "))
#b = int(input("b: "))
#c = int(input("c: "))
#count = 0
#if a % 2 == 0:
#    count+= 1
#if b % 2 == 0:
#    count+= 1
#if c % 2 == 0:
#    count+= 1
#print(count)


#Задача4
#import random
#a = random.randint(9, 99)
#a = str(a)
#print("Случайное двузначное число: ", a)
#if int(a[0] + a[1]) >= 10:
#    print("Да")
#else:
#    print("упс")


#Задача5
#a = 10
#n = 20
#for i in range(n):
#    print(a)

#или

#s = 10
#n = 20
#while n:
#    print(s)
#    n -= 1

#Задача6
#a = int(input("Введите число: "))
#i = 1
#while i < a:
#    print(i**3, end=' ')
#    i += 1

#Задача7
#pr = 1
#for i in range(5,21):
#    pr *= i
#print(pr)

#Задача8
#n = int(input("Введите число: "))
#for i in range(1, n + 1):
 #  if i ** 2 <= n:
#       print(i ** 2, end=' ')

#Задача9
#number_max = int(input("Введите натуральное число: "))
#min_number = min(str(number_max))
#print(min_number)

#Задача10
#year = int(input("Введите год : "))
#if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#    print("Високосный")
#else:
#    print("Не високосный")

#Задача11
#cows = int(input("Введите кол-во коров: "))
#if cows in range(11, 15):
#        print(cows, 'коров')
#else:
#        temp = cows % 10
#        if temp in list(range(5, 10))+[0]:
#                print(cows, 'кооров')
#        if temp == 1:
#                print(cows, 'корова')
#        if temp in range(2, 5):
#                print(cows, 'коровы')