
#Task_1
#with open('in.txt', 'r', encoding='utf-8') as f:
#    result = '\n'.join(map(lambda x: f'{x}!', f.read().split('\n')))
#print(result)

#Task_2
#f_1 = open('input.txt', 'r', encoding='utf-8')
#spl = f_1.readline().split()
#f_1.close()
#x, y, q, w, e, r, t, u, i, o = int(spl[0]), int(spl[1]), int(spl[2]), int(spl[3]), int(spl[4]), int(spl[5]), int(spl[6]), int(spl[7]),int(spl[8]), int(spl[9])
#p=x*y*q*w*e*r*t*u*i*o
#f_2 = open("output.txt","a" )
#f_2.write(str(p))
#f_2.close()
#print(p)


#Task_3
#использовать json
#import json
#from datetime import datetime

#current_date = datetime.now()

#with open("goods.json") as json_file:
#    goods = json.load(json_file)
#    for info_good in goods["goods"]:
#        date_data = datetime(*list(map(int, info_good["date"].split("-"))))

#    if info_good["cost"] > 1000000:
#         print(info_good)

#    elif int(str(current_date - date_data).split()[0]) > 30:
#         print(info_good)


#Task_6
#try:
#    x = (1, 2, 5, 7)
#    x = x / 2
#    print(x)
#except TypeError:
#    print("error types")

#Task_7
#try:
#    s = ['l', 'i', 's', 't']
#    print(s[4])
#except IndexError:
#    print("list index out of range")


#Task_8
#try:
#    current_year_message = 'Year is '
#    current_year = 2023
#    print(current_year_message + current_year)

#except TypeError:
#    print("concatenate str to str")


#Task_9
#try:
#    file = open('123.txt', encoding='utf-8')
#    s = file.readline()
#    print(s)
#    file.close()
#except FileNotFoundError:
#    print("file not found")


#Task_10
#try:
#    numbers = [10, 20, 30, 40, 50]
#    deleted_element = numbers.pop("2")
#    print(deleted_element)
#except TypeError:
#    print("object cannot be interpreted as an integer")


#Task_11
#with open("7.txt", 'r') as f:
#    s = list(map(lambda i: i.strip('.,!?'), f.read().lower().split()))
#    m = max(sorted(s), key=lambda j: s.count(j))
#    print("%s %d" % (m, s.count(m)))


#Task_12
#import re

#with open('8.txt', 'r+') as f:
#    a = re.split(r"(\d+)", f.readline())[:-1]
#    result = ''.join([y * int(x) for x, y in zip(a[1::2], a[::2])])
#    print(result)
#    f.seek(0)
#    f.write(result)
