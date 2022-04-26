# Множественное наследование - это когда дочерний класс наследуется от двух или более классов.
# MRO - (METHOD RESOLUTION ORDER) -порядок разрешения методов, поиск родительских классов. Был создан для решения проблемы ромба (С3). 
# Локальное старшинство -порядок при котором класс написанный первее наследуется первее.


# class Auto:
#     def play_music_at_station(self):
#         print('Music is playing')
#     def ride(self):
#         print('We are riding on the ground!')

# class Plane:
#     def fly(self):
#         print('We are flying!')
    
#     def play_music_at_station(self):
#         print('We started to listen to music!')

# class FutureAuto(Auto, Plane):
#     pass 

# obj1 = FutureAuto()
# obj1.fly()
# obj1.ride()
# obj1.play_music_at_station()
#-----------------------------------------------------------------------------------------------------

# class Zero:
#     def say(self):
#         print('class Zero')

# class First:
#     pass
#     # def say(self):
#     #     print('class First')

# class Second(First,Zero):
#     pass
#     # def say(self):
#     #     print('class Second')

# class Third(Zero):
#     def say(self):
#         print('class Third')

# class Forth(Second, Third):
#     def say(self):
#         super().say()
#         print('class fourth')
# obj = Forth()
# obj.say()
# print(Forth.__mro__)

# class Y:
#     pass
# class X:
#     pass
# class A(X,Y):
#     pass
# class B(Y,X):
#     pass
# class G(A,B):
#     pass
# class MyMRO(type):
#     def mro(cls):
#         return (cls, A,B,X,Y, object)

# class G(A,B, metaclass=MyMRO):
#     def say(self):
#         print('hello')
# obj = G()
# obj.say()
#----------------------------------------------------------------------------------------------------

#Mixins(Миксины)
# class MusicPlayerMixin():
#     def play_music_on_station(self):
#         print('Music is playing')

# class Machines:
#     def start_engine(self):
#         print('started engine')

# class Auto(Machines,MusicPlayerMixin):
#     # def play_songs_on_station(self):
#         # print('Music is playing')
#     pass

# class Plane(Machines):
#     pass 

# class Boat(Machines):
#     pass

# class Smartclock(Machines,MusicPlayerMixin):
#     def play_song_on_station(self):
#         print('Music is playing')
# obj = Auto()
# obj.play_songs_on_station()
#-----------------------------------------------------------------------------------------------------

# SOLID - 0 (OPEN/CLOSED PRINCIPLE)- принцип открытости и закрытости
# Классы, функции должны быть открыты для расширения но закрыты для изменения
 
# class flyMixin:
#     def fly():
#         print('Мы можем лететь до 500км в час в воздухе')

# class Car(flyMixin):
#     def ride():
#         print('Мы можем разогнаться до 250км\ч')

# class SportCar(Car):
#     def ride():
#         print('мы можеи разогнаться дл 500км в час')

# Car.ride()
# Car.fly()












