# ООП (объектно-ориентированное програмирование) - целью создания была связать поведение объекта с ее данными 

# Класс - это описание того, какими свойствами и поведением должен обладать объект либо экземпляр. А объект это экземпляр с собственным состоянием этих свойств

# Свойствами называют обычные переменные(body='человеческое тело, name= 'Акмарал)

# Поведение- это обычные функции(def eat - методы)
#-----------------------------------------------------------------------------------------------------

# class Dog:
#     #атрибуты класса 
#     name = "Bobik"
#     age = 7

# bobik = Dog() #здесь определяется объект класса присвоенный в переменную bobik
# belka = Dog()

# print(bobik.name)
# print(bobik.age)
# print(belka.name)
# print(belka.age)

# class Dog():
#     ushi = 'Есть уши'
#     # в self  хранится сам объект 
#     def __init__(self, name, age, color):
#         '''
#         Инициализатор .
#         Именно здесь определяются атрибуты объекта класса 
#         '''
#         self.name = name #Атрибут экземпляра (объекта) класса 
#         self.age = age
#         self.color = color

# bobik = Dog('Бобик', '7', 'коричневого')
# strelka = Dog('Стрелка', '3', 'белого')
# # print(bobik.color)
# # print(strelka.color)
# # print(bobik.ushi)
# # bobik.ushi = 'нет ушей'
# # print(bobik.ushi)
# # print(strelka.ushi)

# print(f'У меня есть собака по кличке {bobik.name}. Ему {bobik.age} лет. Он {bobik.color} цвета. И у него {bobik.ushi}')



# class Human:
#     def __init__(self, name, weight, nationality) -> None:
#         self.name = name
#         self.age = 0
#         self.weight = weight
#         self.nationality = nationality

#     def birthday(self):
#         import random 
#         print(f'Happy birthday! {self.name}')
#         self.age += 1 #age = age + 1
#         self.weight += random.randint(3,7)

# human1 = Human('John', 3.700, 'American')
# human2 = Human('Abubakr', 3, 'Arabic')

# # print(id(human1))
# # print(id(human2))

# print(human1.name, human1.age, human1.weight, human1.nationality)
# print(human2.name, human2.age, human2.weight, human2.nationality)

# print('after 1 year:')
# human1.birthday()
# human2.birthday()

# print(human1.name, human1.age, human1.weight, human1.nationality)
# print(human2.name, human2.age, human2.weight, human2.nationality)


# print('after 3 month: ')
# human1.birthday()
# print(human1.name, human1.age, human1.weight, human1.nationality)
# print(human2.name, human2.age, human2.weight, human2.nationality)


# class Student:
#     university = 'KRSU'

#     def __init__(self, first_name, last_name) -> None:
#         self.name = first_name
#         self.last = last_name
#         self.books = []
#         self.languages = {}
#         self.knowledge = 0
#         self.is_ready_to_work = False
#     def add_points(self, point):
#         self.knowledge += point
#         if self.knowledge > 500:
#             self.is_ready_to_work = True
#             print(f'{self.name} is ready to work!!!')

#     def read_book(self, book):
#         self.books.append(book)
#         self.add_points(50)
    
#     def do_homework(self):
#         self.add_points(50)
    
#     def do_real_project(self):
#         self.add_points(100)
    
#     def learn_new_languages(self, language, point):
#         if not 0< point <= 100:
#             raise Exception('Your point out of range!')
#         self.languages.update({language: point})
#         self.add_points(100)
# st1 = Student('John', 'Snow')
# st2 = Student('Jamie', 'Lanister')
# print(st1.name)
# print(st2.name)
# print('Before study John:', st1.is_ready_to_work)
# st1.read_book('Game of Thrones')
# st1.read_book('Martin Iden')
# st1.read_book('Eugene Onegin')
# st1.read_book('Richest man in Vavilon')
# st1.do_real_project()
# st1.do_homework()
# st1.do_homework()
# st1.learn_new_languages('Python', 90)
# print(st1.name, st1.books, st1.knowledge, st1.languages)
# print(st1.university)

# class Salary:
#     tax = 15
#     def __init__(self, salary, experience) -> None:
#         self.salary = salary
#         self.experience = experience

#     def total_tax(self):
#         tax = ((self.experience*12)*self.salary/100)*15
#         return f' сумма вашего налога составляет {tax} сом'

# human1 = Salary(500, 4)
# # print(human1.salary)
# # print(human1.experience)
# print(human1.total_tax())


# class Salary:
#     tax = 0.15
#     def __init__(self,salary, exp)-> None:
#         self.salary = salary
#         self.experience = exp
    
#     def sum_of_tax(self):
#         result = (self.salary*self.tax)*self.experience
#         print(f'сумма налога составила {result}сом, за {self.experience} лет!')

# John = Salary(150000, 10)
# John.sum_of_tax()

class Password:
    def __init__(self, password) -> None:
        self.password = password
    
    def validate(self):
        if not len(self.password) in range(8,16):
            raise Exception('Too short or too long password')
        has_digits = False
        has_letters = False
        has_specials = False
        
        for ch in self.password:
            if ch.isdigit():
                has_digits = True
            elif ch.isalpha():
                has_letters = True
            elif ch in {'@', '#', '&', '$', '%', '!', '~', '*'}:
                has_specials = True
        if has_digits and has_letters and has_specials:
            print(f'Validation passed')
        else:
            raise Exception('Validation error')
        
        has_digits = len(tuple(filter(lambda ch: ch.isdigit(), self.password))) != 0

        


password = Password('123456789')
password.validate()




