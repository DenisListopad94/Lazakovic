#Задача1
#from random import randint
#def func():
#    print([randint(1,10)**2 for i in range(1, 11)])
#func()


#Задача2
#def numbers():
#    for i in range(100, 1000):
#        if i % 3 == 0 and i % 5 == 0:
#            print(i)
#numbers()


#Задача3
#def new_list():
#    numbers = input().split()
#    print([i**int(numbers[-1]) for i in range(int(numbers[0]), int(numbers[1]))])
#new_list()


#Задача5
#def numbers(x, y):
#    return(min(x, y))
#result = numbers(numbers(43,88), numbers(44, 81))
#print(result)


#Задача6
#from math import sqrt
#def distance(x1, y1, x2, y2):
#    return sqrt((x1 -x2)**2 + (y1 - y2)**2)
#x1 = float(input())
#x2 = float(input())
#y1 = float(input())
#y2 = float(input())
#print(distance(x1, y1, x2, y2))


#Задача7
#def fib(n):
#     first_number = next_number = 1
#     for i in range(2, n):
#          first_number, next_number = next_number, first_number + next_number
#     print(next_number)

#print(fib(11))


#Задача8
#def closet_mod_5(x):
#     if x % 5 == 0:
#          return
#     else:
#          return (x//5+1)*5
#print(closet_mod_5(1))


#Задача9
#def modify_list(l):
#     l = [i // 2 for i in l if i % 2 == 0]
#modify_list([5, 7, 9, 8, 11, 12])


#Задача11
#lst = []
#count = 0
#for i in range(1, 101):
#     for j in range(1, i + 1):
#         if i % j == 0:
#             count += 1
#     if count == 2:
#         lst.append(i)
#     count = 0
#print(lst)