# len()- полиморфная функция 

# print(len('makers'))
# print(len([1,2,3,4,5]))

# + - полиморфный оператор
# print(5 + 5)
# print('Hello' + 'world')

# Полиморфизм - суть использования заключается в использовании единственной сущности (метод, функции, оператор или объекты) для представления различных типов в различных сценариях. 


# class Cat:
#     def __init__(self,name, age) -> None:
#         self.name = name
#         self.age = age
    
#     def info(self):
#         print(f'Я кошка. Меня зовут {self.name}, и мне {self.age}')

#     def sound(self):
#         print('Мяу!')
# class Dog:
#     def __init__(self, name, age) -> None:
#         self.name = name
#         self.age = age
    
#     def info(self):
#         print(f'Я собака. Меня зовут {self.name}, и мне {self.age}')

#     def sound(self):
#         print('Гав!')

# cat = Cat('Murka', 5)
# dog = Dog('Pluto', 9)

# for animal in(cat, dog):
#     animal.info()
#     animal.sound()
#-----------------------------------------------------------------------------------------------------
# Абстракция (абстрактный класс) - его можно рассматривать как набор методов, которые должны быть созданы в любых дочерних классах, построенных на основе абстрактного класса. 
# Абстрактный метод - это метод у которого есть объявление но нет реализации. 

# from abc import ABC, abstractmethod 

# class Animal(ABC):
#     @abstractmethod
#     def eat(self):
#         pass 

# class Giraffe(Animal):
#     def eat(self):
#         print('Я кушаю листву !')

# class Panther(Animal):
#     def eat(self):
#         print('я кушаю много мяса!')

# obj1 = Giraffe()
# obj2 = Panther()
# obj1.eat()
# obj2.eat()
#-----------------------------------------------------------------------------------------------------

# from math import pi
# from abc import ABC, abstractmethod

# class Shape(ABC):
#     def __init__(self, name) -> None:
#         self.name = name
#     @abstractmethod
#     def area(self):
#         pass

#     def fact(self):
#         print('Я некая фигура в двумерной плоскости')

# class Square(Shape):
#     def __init__(self, lenght) -> None:
#         super().__init__('квадрат')
#         self.length = lenght

#     def area(self):
#         print(self.length ** 2)
    
#     def fact(self):
#         print('У меня все углы равны 90 градусам')

# class Circle(Shape):
#     def __init__(self,radius) -> None:
#         super().__init__('окружность')  
#         self.radius = radius

#     def area(self):
#         print(pi * self.radius ** 2) 

# a = Square(4)
# b = Circle(3)
# print(a.name)
# print(b.name)
# a.fact()
# b.fact()
# b.area()
# a.area()
#-----------------------------------------------------------------------------------------------------
# SOLID - L LISKOV SUBSTITUTION PRINCIPLE 
# Принцип подстановки Барбары Лисков

# Цель принципа - это убедиться в том что подкласс может занять место своего родителя без ошибок
# Если код обнаруживает, что есть проверка на тип класса, то тогда ваш код нарушает принцип подстановки 
    


# from math import pi
# from abc import ABC, abstractmethod

# class Shape(ABC):
#   def __init__(self, name) -> None:
#       self.name = name
#   @abstractmethod
#   def get_area(self):
#       pass
      
# class Triangle(Shape):
#   def __init__(self,main_part, height):
#     super().__init__('треугольник')
#     self.main_part = main_part
#     self.height = height

#   def get_area(self):
#     print(0.5 * self.main_part * self.height)
    
# class Square(Shape):
#   def __init__(self, lenght) -> None:
#       super().__init__('квадрат')
#       self.length = lenght

#   def get_area(self):
#       print(self.length ** 2)
    

# class Circle(Shape):
#   def __init__(self,radius) -> None:
#       super().__init__('окружность')  
#       self.radius = radius

#   def get_area(self):
#       print(pi * self.radius ** 2) 

# a = Triangle(5,6)
# b = Square(4)
# c = Circle(3)
# print(a.name)
# print(b.name)
# print(c.name)
# a.get_area()
# b.get_area()
# c.get_area()
















