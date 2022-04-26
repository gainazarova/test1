# Инкапсуляция
# 1. Связь данных с методами которые этими данными управляют.
# 2. Набор инструментов для управления доступом или методами которые управляют этими данными. 

# Инкапсуляция как связь 
# class Phone:
#     number = '+996777777777'
#     def print_number(self):
#         print(f'мой номер : {self.number}')
# my_phone = Phone()
# my_phone.print_number()    
# 
# Инкапсуляция как управление доступом 
# 3 уровня доступа в питоне: 
#     1. публичный (public)- number
#     2. защищенный (_protected , parent/child) - _number   #нижний слеш значит защищенный
#     3. приватный (__private, частный только в текущем классе, вообще не наследуется) - __number  #два нижних слеша означает приватный

# class Car:
#     def __init__(self) -> None:
#         self.marka = 'Honda' #PUBLIC 
#         self._model = 'Fit'  #PROTECTED
#         self.__motor = 'ABC'  #PRIVATE

# class Audi(Car):
#     pass
# car1 = Audi()
# print(car1.marka)
# print(car1._model)
# print(car1.__motor)
# car = Car()
# print(car.marka)
# print(car._model)
# print(car.__motor)
# car.marka = 'BMW'
# print(car.marka)
# car._model = 'Accord'
# print(car._model)
# car.__motor = 'QWERTY'
# print(car.__motor)


# class Phone:
#     username = 'John'
#     _caller = 'Stark'
#     __count_of_calls = 15
#     def call(self):
#         print(f'тебе звонит {self._caller}')
#     def turn_on(self):
#         self.__count_of_calls += 1
#         print('Алоо вотс ап бро !')
# phone = Phone()
# print(phone.username)
# phone.call()
# print(phone._caller)
# phone.turn_on()
# # print(phone.__count_of_calls)
# print(phone._Phone__count_of_calls)

#getter and setter 
# Они используются для получения и установки значения, чтобы добавить логику проверки при получении данных. 
# Еще чтобы избежать прямого доступа к защищенному полю класса 


# class Person:
#     def __init__(self,name) -> None:
#         self.name = name
#         self.age = 0
    
#     def display_info(self):
#         print(f'Имя: {self.name}\nВозраст: {self.age}')

# john = Person('John')
# print(john.name)
# print(john.age)
# john.display_info()
# john.name = 'Gulchatai'
# john.age = -18
# print(john.name)
# print(john.age)


# class Person:
#     def __init__(self,name) -> None:
#         self.name = name
#         self.__age = 0
    
#     def display_info(self):
#         print(f'Имя: {self.name}\nВозраст: {self.__age}')

#     def set_age(self,age):   #setter
#         if 0 < age <140:
#             self.__age = age
#         else:
#             print('Недопустимый возраст!')
#     def get_age(self): return self.__age #getter
# tom = Person('Tom')
# tom.display_info()
# tom.set_age(18)
# print(tom.get_age())
# tom.display_info()

# Аннотация свойств 
# @property

# class Person:
#     __name = 'John'
#     __age = 22

#     @property 
#     def name(self):
#         print(self.__name)

    
#     @name.setter
#     def name(self, name):
#         self.__name = name

#     @property
#     def age(self):
#         print(self.__age)

#     @age.setter
#     def age(self,age):
#         if 0 < age < 150:
#             self.__age = age
#         else: print('Недопустимый возраст')

# obj = Person()
# obj.name
# obj.name = 'Tom'
# obj.name
# obj.age
# obj.age = 20
# obj.age 
#----------------------------------------------------------------------------------------------------
# SOLID = I (INTERFACE SEGREGATION PRINCIPLE)
# Принцип разделения интерфейса 
# Интерфейс -Абстрактный класс 
# Пользователь - это у нас дочерний класс 

# не создавайте слишком большие абстрактные классы, создавайте маленькие абстракции.
# не наследуйтесь от  абстрактных  классов которые не будут использованы в  дочерних  классах.  


# class A:
#   def method1(self):
#     print('Hello world')
# class B(A):
#   pass
# ex = B()
# ex.method1()


# class Human:
#   def __init__(self):
#     self.name = 'Marie'
#     self._age = 22
#     self.__nationality = 'Russia'

#   def get_nationality(self):
#     return self.__nationality
# per1 = Human()
# print(per1.name)
# print(per1._age)
# print(per1.get_nationality())


# class Car:
#   def __init__(self, speed):
#     self.__speed = speed

#   def set_speed(self, speed):
#     if 0<speed<240:
#       self.__speed = speed
#     else:
#       print('Скорость превышает указанный лимит!')

#   def show_speed(self):
#     return self.__speed
# ex = Car(180)
# ex.set_speed(180)
# ex.show_speed()

# class Car:
#   def set_speed(self, speed):
#       self.__speed = speed
#   def show_speed(self):
#     return self.__speed
# ex = Car()
# ex.set_speed(180)
# print(ex.show_speed())


# class Car:
#   def set_speed(self, speed):
#       self.__speed = speed
  
#   def show_speed(self):
#     return self.__speed
# ex = Car()
# ex.set_speed(180)
# print(ex.show_speed())


