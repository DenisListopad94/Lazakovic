#Task_1
#class Сalculate:
#     number_1 = 5
#     number_2 = 7

#     def number(self):
#         print(f'Число 1: {self.number_1}, число 2: {self.number_2}')

#     def change(self, new_number_1: int, new_number_2: int) -> tuple:
#         self.number_1 = new_number_2
#         self.number_2 = new_number_2
#         return new_number_1, new_number_2

#     def num_sum(self):
#         sum = self.number_1 + self.number_2
#         print(f'Сумма двух чисел равна: {sum}')

#     def equality(self):
#         if self.number_1 < self.number_2:
#             print(f'Число - {self.number_2} > {self.number_2}')
#         elif self.number_1 == self.number_2:
#             print(f'Число - {self.number_1} равно числу - {self.number_2}')
#         else:
#             print(f'Число - {self.number_1} > {self.number_2}')


#Task_2
#class Сounter():
#     def __init__(self, start_value=0, min_value=0, max_value=100):
#         self.start_value = start_value
#         self.min_value = min_value
#         self.max_value = max_value
#         self.value = start_value

#     def current_value(self):
#         return self.value

#     def increase(self):
#         if self.value < self.max_value:
#             self.value += 1
#         else:
#             print("Maximum value")

#     def decrease(self):
#         if self.value > self.min_value:
#             self.value -= 1
#         else:
#             print("Minimum value")


#Task_3
#class Shop:
#     def __init__(self, *products):
#         self.products = list(products)

#     def search_product(self, product):
#         if product in self.products:
#             print(f"Продукт есть в магазине")
#         else:
#             print(f"Продукт отсутствует в магазине")

#     def add_product(self, new_product):
#         if new_product in self.products:
#             print("Продукт есть в каталоге магазина")
#         else:
#             self.products.append(new_product)
#             print("Продукт добавлен в каталог")
#
#     def del_product(self, product):
#         if product in self.products:
#             self.products.remove(product)
#             print("Продукт удален")
#         else:
#             print()


#Task_4
#class MoneyBox:
#    def __init__(self, capacity):
#        self.capacity = capacity
#        self.count = 0
#    def can_add(self, number):
#        return self.count + number <= self.capacity

#    def add(self, number):
#        if self.can_add(number):
#            self.count += number
#            print(f"Добавлено {number} монет. Текущее количество монет: {self.count}")
#        else:
#            print("Копилка переполнена.")
