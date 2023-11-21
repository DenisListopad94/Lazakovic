#Задача1
#tup = (6, 2, 7, 8)
#for number in tup:
#    counter = 0
#    for i in range(1, number):
#        if number % i == 0:
#           counter += i
#    if counter == number:
#                print('Совершенное число:', number)



#Задача2
#tup = (5, 2, -2, 7, -8, -9, 1)
#counter = 0
#for number in range(len(tup) -1):
#    if tup[number] < 0 and tup[number+1] > 0 or tup[number] > 0 and tup[number+1] <0:
#        counter +=1
#print(counter)


#Задача3
#lst_1 = [4, 1, 6, 9]
#lst_2 = [8, 1, 2, 4, 9, 5, 7, 6]
#lst_3 = ()
#for number in lst_1:
#    if number not in lst_2:
#        lst_3.append(number)
#        print(min(lst_3))
#else:
#    print("Нет такого элемента")


#Задача4
#lst = [9, 18, 331, 34, 145]
#lst_new = []
#for number in lst:
#    lst_new.append(number)
#    if number % 2 == 0:
#        number = int(str(number)[::-1])
#        lst_new.append(number)
#print(lst_new)


#Задача5
#lst = [5, 2, 4, 5, 1, 2]
#for i in set(lst):
#    print(i, "встречается", lst.count(i))


#Задача6
#lst = [7, 4, 1]
#lst_new = []
#for i in lst:
#    lst_new.append(i)
#    lst_new.append(0)
#print(lst_new)


#Задача7
#numbers = '1 3 1 3 4 8'
#new_numbers = set()
#numbers_2 = numbers.split()
#for i in numbers_2:
#    if i in new_numbers:
#        print("YES")
#    else:
#         new_numbers.add(i)
#         print("NO")



#Задача8
#import random
#n = int(input("enter n:"))
#rand_numb = random.randint(1, n)
#numbers = set()
#for i in range(1, n +1):
#    numbers.add(i)
#while True:
#    print(numbers)
#    numb = set(map(int, input().split()))
#    if rand_numb in numb:
#        print("Yes")
#        numbers = numb.copy()
#        if len(numbers) == 1:
#            print(f"your number {rand_numb}")
#            break
#    else:
#        print("No")
#        numbers -= numb


#Задача9
#dict = {"answer":"report", "big":"huge", "angry":"mad", "calm":"still"}
#word = input("Enter a word to find a synonym: ")
#for i in dict:
#    if i == word:
#        print(dict[i])
#    if dict[i] == word:
#        print(i)





