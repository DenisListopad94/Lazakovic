#Task_1
#class Task:
#    def __init__(self, description, status,deadline):
#        self.description = description
#        self.status = status
#        self.deadline = deadline

#    def mark_is_done(self):
#        self.status = "Done"

#class Project:
#    def __init__(self, name, task):
#        self.name = name
#        self.task = task

#    def add_task(self, task):
#       self.task.append(task)

#    def show_task(self):
#         print(f"Tasks in project '{self.name}':")
#         for task in self.task:
#             status_str = "completed" if task.status else "not completed"
#             print(f'{task.description} {task.deadline}: {status_str}')

#class ProjectManager:
#    def __init__(self):
#        self.project = []
#    def create_project(self, name, task):
#        project = Project(name, task if task else [])
#        self.project.append(project)
#        return project



#Task_2
#class Passenger:
#    def __init__(self, name, surname):
#        self.name = name
#        self.surname = surname
#class Ticket:
#    def __init__(self, passenger, flight_info):
#        self.passenger = passenger
#        self.flight_info = flight_info

#class Flight:
#    def __init__(self):
#        self.tickets = []

#class Airline:
#    def __init__(self, name):
#        self.name = name
#        self.flights = []

#    def booking_ticket(self, passenger):
#      ticket = Ticket(passenger, self.flight_info)
#      self.ticket.append(ticket)
#      return ticket

#    def cancell_ticket(self, ticket):
#        self.ticket.remove(ticket)

#    def show_tickets(self):
#        print(f'Reserved flight tickets {self.name}:')
#        for ticket in self.ticket:
#            print(f'{ticket.passenger.name} {ticket.passenger.surname} - {ticket.flight_info}')


#Task_3
# from abc import ABC, abstractmethod
# import random
#
# class Alive(ABC):
#     def __init__(self, age_limit):
#         self.age = 0
#         self.age_limit = age_limit
#         self.alive = True
#
#     @abstractmethod
#     def eat(self, food_available):
#         pass
#
#     def is_alive(self):
#         return self.alive and self.age < self.age_limit
#
# class Fox(Alive):
#     def __init__(self):
#         super().__init__(age_limit=5)
#
#     def eat(self, food_available):
#         if food_available:
#             print("Fox is eating a rabbit.")
#         else:
#             print("Fox has no food.")
#             self.alive = False
#
# class Rabbit(Alive):
#     def __init__(self):
#         super().__init__(age_limit=3)
#
#     def eat(self, food_available):
#         if food_available:
#             print("Rabbit is eating a plant.")
#         else:
#             print("Rabbit has no food.")
#             self.alive = False
#
# class Plant(Alive):
#     def __init__(self):
#         super().__init__(age_limit=10)
#
#     def eat(self, food_available):
#         if food_available:
#             print("Plant is absorbing sunlight.")
#         else:
#             print("Plant has no sunlight.")
#             self.alive = False
#
# fox = Fox()
# rabbit = Rabbit()
# plant = Plant()
#
# for _ in range(6):
#     fox.eat(random.choice([True, False]))
#     fox.age += 1
#     print(f"Fox is alive: {fox.is_alive()}")
#
# for _ in range(4):
#     rabbit.eat(random.choice([True, False]))
#     rabbit.age += 1
#     print(f"Rabbit is alive: {rabbit.is_alive()}")
#
# for _ in range(11):
#     plant.eat(random.choice([True, False]))
#     plant.age += 1
#     print(f"Plant is alive: {plant.is_alive()}")