#Task_1
#x = lambda subtitle, title: subtitle in title
#title_text = input("Введите текст строки: ")
#subtitle_text = input("Введите текст подстроки: ")
#result = x(subtitle_text, title_text)
#print(result)


#Task_2
#f = lambda number: not number % 2
#print(f(10))


#Task_3
#greetings = lambda name: f"Привет, {name}!" if name and name[0].isupper() else "Неверно введенное имя"
#entering_name = input("Введите имя: ")
#result = greetings(entering_name)
#print(result)

#Task_4
#def digits(n):
#    while n > 0:
#        print(n % 10, end=" ")
#        n = n//10
#print(digits(14623))


#Task_5
#from math import log
#def is_power(n):
#    Logn = log(n, 2)
#    if (Logn == int(Logn)):
#        print("True")
#    else:
#        print("False")
#print(is_power(1048576))


#Task_6
#def sum_numbers(n):
#    if n > 10:
#        return n % 10 + sum_numbers(n // 10)
#    else:
#        return n

#print(sum_numbers(14623))


#Task_7
#from time import time
#def time_decorator(func):
#    def wrapper():
#        start_time = time()
#        func()
#        end_time = time()
#        finaly_time = end_time - start_time
#        print(f"Execution time: {finaly_time} seconds")
#    return wrapper

#@time_decorator
#def print_primes():
#    for num in range(2, 101):
#        is_prime = all(num % i != 0 for i in range(2, int(num**0.5) + 1))
#        if is_prime:
#            print(num)
#print_primes()


#Task_9
#def numbers(num, ans=2, rec=[]):
#    if num < ans * ans:
#        print(rec + [num])
#        return
#    if num % ans == 0:
#        return numbers(num // ans, ans, rec + [ans])
#    else:
#        return numbers(num, ans + 1, rec)
#numbers(18)
