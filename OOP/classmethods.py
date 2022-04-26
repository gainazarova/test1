# Создайте класс мобильного телефона. Определите непубличные атрибуты для imei, уровня заряда батареи, краткой информации об установленной ОС. Изначальный уровень заряда
# батареи – 100%, он не может опуститься ниже 0. Методы доступа к данным расходуют 
# 0,5 % заряда при каждом обращении.
# Определите 2 публичных метода: для прослушивания музыки, и для просмотра видео.
# При каждом прослушивании музыки расходуется 5% заряда, а при просмотре видео – 7%.
# Если заряд достигает уровня ниже 10% - не давайте пользователю просматривать видео. При
# полной разрядке все методы телефона не доступны (выбрасывайте ошибку, что телефон
# разряжен).
# Также предусмотрите возможность зарядки батареи.


# class Phone:
#     def __init__(self,imei, os) -> None:
#         self._imei = imei 
#         self._os_info = os
#         self.__battery_level = 100

#     def get_info(self):
#         if self.__battery_level <= 0:
#             raise Exception('Телефон разряжен!!!')

#         if self.__battery_level - 0.5 < 0:
#             self.battery_level = 0
#             raise Exception('Телефон разряжен')

#         self.__battery_level -= 0.5
#         print(f'OS: {self._os_info}\nImei: {self._imei}')

#     @property
#     def battery_level(self):
#         if self.__battery_level <= 0:
#             raise Exception('Телефон разряжен!!!')
        
#         if self.__battery_level - 0.5 < 0:
#             self.battery_level = 0
        
#             raise Exception('Телефон разряжен')
            
#         self.__battery_level -= 0.5
#         print(f'Уровень заряда :{self.__battery_level}')

#     @battery_level.setter
#     def battery_level(self, charge_level):
#         if self.__battery_level < charge_level and charge_level <= 100:
#             self.__battery_level = charge_level
#             print(f'Телефон заряжен на {self.__battery_level} процентов!')
#         else:
#             raise Exception('Вы не можете разряжать уровень батареи!')
    
#     def play_music(self):
#         if self.__battery_level<= 0:
#             raise Exception('Телефон разряжен!!!')
#         if self.__battery_level - 5 < 0:
#             self.battery_level = 0
#             raise Exception('Телефон разряжен!')
        
#         self.__battery_level -= 5
#         print('Слушаем музыку!')
    
#     def play_video(self):
#         if self.__battery_level <= 0:
#             raise Exception("Телефон разряжен!!!")

#         if self.__battery_level <= 10:
#             print("У вас недостаточно заряда батареи для просмотра видео!")

#         self.__battery_level -= 7
#         print('Смотрим видео!')      

# apple = Phone('123456789', 'IOS')
# apple.play_video()
# apple.play_music()
# apple.get_info()
# for x in range(1,18):
#     apple.play_music()
# apple.battery_level
# apple.battery_level = 90
# apple.battery_level
# #----------------------------------------------------------------------------------------------------
# Class methods, instance methods, static methods

# методы экземпляра класса (instance methods) это те методы в ООП которые могут изменять состояние экземпляра класса: def methods(self)

# методы класса (class methods) - это те методы которые могут изменять состояние самого класса:
# @classmethods - это декоратор который оюозначает что метод является методом класса #def method(cls) -cls это ссылка на сам класс 

# статистические методы (Static methods) -это те методы которые не могут изменять состояние как экземпляра класса так и самого класса:
# @staticmethod -это декоратор который обозначает статистический метод 
# #def method()

# class Person:
#     surname = 'Snow'
#     def __init__(self, name, age) -> None:
#         self.name = name
#         self.age = age 
    
#     @classmethod
#     def from_birth_date(cls,name,year):
#         print(cls, '!!!!')
#         from datetime import date
#         cls.surname = 'Lanister'
#         age = date.today().year - year
#         return cls(name, age) 
    
#     @staticmethod
#     def isAdult(age):
#         if age >= 18:
#             print('Человек совершеннолетний')
#         else:
#             print('Нет не совершеннолетний')
# john = Person('John', 24)
# print(john.name)
# print(john.surname)
# Person.isAdult(john.age)
# john.isAdult(17)

# jamie = Person.from_birth_date('Jamie', 1988)
# print(jamie.name)
# print(jamie.surname)
# print(jamie.age)
# Person.isAdult(jamie.age)

# sansa = Person('Sansa', 19)
# print(sansa.name)
# print(sansa.surname)

# class Date:
#     def __init__(self, day, month, year) -> None:
#         self.day = day
#         self.month = month
#         self.year = year

#     @classmethod
#     def date_from_string(cls, stroka):
#         day, month, year = map(int, stroka.split('.'))
#         return cls(day, month, year)

#     def string_to_db(self):
#         return f'{self.year} - {self.month} - {self.day}'

# date = Date(15, 4, 2022)
# print(date.string_to_db())
# string_date = '15.04.2022'
# day, month, year = map(int, string_date.split('.'))
# # print(day, month, year)
# date1 = Date(day, month, year)
# print(date1.string_to_db())
# date2 = Date.date_from_string('9.05.2022')
# print(date2.string_to_db())




