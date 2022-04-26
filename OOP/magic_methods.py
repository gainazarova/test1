
# Magic methods
# Dunder methods-(double underscore) - __init__
# Служебные методы

# res = 5 + 5  #__add__ 
# print(res)

# class A(int):
#     pass 
# obj = A()
# print(dir(obj))

# Магические методы сравнения 
# __eq__(self,other)-> ==
# __ne__(self,other)-> !=
# __lt__(self,other)-> <
# __gt__(self,other)-> >  #7 > 6
# __le__(self,other)-> <=
# __ge__(self,other)-> >=

# class Word(str):
#     def __init__(self, word) -> None:
#         self.word = word
    
#     def __gt__(self, other:str)-> bool:
#         print('__gt__ сработал!')
#         return len(self) > len(other) 

#     def __lt__(self, other:str)-> bool:
#         print('__lt__ сработал!')
#         return  len(self)<len(other)
    
#     def __eq__(self, other: object) -> bool:
#         print('сработала функция __eq__!')
#         return len(self) == len(other)

# word1 = Word('John')
# word2 = Word('Tom123')
# # result = word1 > word2
# # print(result)
# # print(word1 < word2)
# # print(word1 == word2)
# print('John' < 'Tom')

# print(ord('J'))
# print(ord('T'))

# Конструктор -> __new__
# Инициализатор -> __init__
# Деструктор -> __del__


# class Converter(float):
#     def __new__(cls, number):
#         return super().__new__(cls, number**2)

#     def __init__(self, number)-> None:
#         self.number = number

# obj = Converter(5.0)
# print(obj.number)
# print(obj+5)

# class Human:
#     def __new__(cls, stroka):
#         return 'stroka' + stroka
#     def __init__(self, stroku) -> None:
#         self.stroka = stroku

# obj = Human('Alpha')
# obj1 = Human()
# print(obj)

# Эти методы нужны для отображения объекта 
# __str__-> Для отображения пользователям
# __repr__-> Для отображения программистам


# class Base:
#     def __init__(self,string)-> None:
#         self.string = string

#     def __repr__(self)-> str:
#         return f'Класс {self.__class__.__name__}\nОбъект:  {self.string}'
    
#     def __str__(self)-> str:
#         return f"Объект {self.string}"
# word = Base('Hello John')
# print(word)
# print(repr(word))
    
# __getitem__ [1,2,3,4,5]
# __setitem__
# __delitem__

# + - * / 

# class Cifra(int):
#     def __new__(cls, number):
#         print('Vyzov new')
#         instance = super().__new__(cls)
#         if not 0<number<100:
#             raise ValueError("Введите число от 0 до 100!")
#         return instance 

#     def __init__(self,number) -> None:
#         self.number = number
    
#     def __add__(self, other):
#         print('Add вызван!')
#         return self.number + other.number
# value1 = Cifra(95)
# value2 = Cifra(15)
# print(value1+value2)


# __sub__ -
# __mul__ *
# __floordiv__ //
# __div__ /
# __mod__ %

   
# class Word(str):
#     def __new__(cls, word):
#         word = word.split(' ')
#         word = ''.join(word)
#         return super().__new__(cls, word)

#     def __init__(self, word) -> None:
#         self.word = word
    
#     def __gt__(self, other:str)-> bool:
#         print('__gt__ сработал!')
#         return len(self) > len(other) 

#     def __lt__(self, other:str)-> bool:
#         print('__lt__ сработал!')
#         return  len(self)<len(other)
    
#     def __eq__(self, other: object) -> bool:
#         print('сработала функция __eq__!')
#         return len(self) == len(other)

# obj = Word('   Hello world   ')
# obj2 = Word('Helloworld')
# print(obj == obj2)

# class Student:
#     def __init__(self,bally) -> None:
#         self.bally = bally
#         self.average_res = (bally['math'] + bally['history'] + bally['literature'] )/3
#     def __gt__(self,other):
#         print(f'сработал  gt : {self.average_res}, {other.average_res}')
#         return self.average_res > other.average_res
# john = Student({'math': 100, 'history': 80, 'literature': 76})
# jamie = Student({'math': 90, 'history': 90, 'literature': 95})
# print(jamie > john)

# class MyList(list):
#     def __init__(self,ls):
#         self.ls = ls

#     def __getitem__(self,index):
#         print(self.ls[index -1])

# x = MyList([1,2,3,4,5])
# x[1]
        





