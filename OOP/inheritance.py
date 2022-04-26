# Принципы в ООП: 
# 1. Наследование
# 2. Инкапсуляция
# 3. Полиморфизм

# #менее значимые
# 4. Абстракция 
# 5. Агрегация
# 6. Композиция

# Наследование - позволяет принимать родительские методы, атрибуты, методы и поведение

# Родительский класс- от которого наследуется
# Дочерний класс- который наследует

# class Employee:
#     bonus = 1.5
#     def __init__(self, name, last_name, salary) -> None:
#         self.name = name
#         self.last_name = last_name
#         self.salary = salary
#     def get_full_name(self):
#         return f'{self.name} {self.last_name}'

#     def get_bonus(self):
#         self.salary = self.salary*self.bonus

# # emp1 = Employee('John', 'Snow', 2000)
# # print(emp1.get_full_name())
# # emp1.get_bonus()
# # print(emp1.salary)

# class Developer(Employee):
#     def __init__(self, name, last_name, salary, prog_lang) -> None:
#         Employee.__init__(self, name, last_name, salary)
#         self.prog_lang = prog_lang

# class Manager(Employee):
#     def __init__(self, name, last_name, salary, emps=None) -> None:
#         super().__init__(name, last_name, salary)
#         if emps == None:
#             self.emps = []
#         else:
#             self.emps = emps 
#     def add_emps(self,emp):
#         if emp not in self.emps:
#             self.emps.append(emp)
#         else:
#             print('Employee is already in the list')
    
#     def show_emps(self):
#         result = []
#         for emp in self.emps:
#             result.append(emp.get_full_name())
#         return result
        
# dev1 = Developer('John', 'Snow', 1500, 'Python')
# dev2 = Developer('Steve','Wozniak', 5000, 'Java')
# dev3 = Developer('Lary','Page', 500, 'JS')
# print(dev1.get_full_name())
# dev1.get_bonus()
# print(dev1.prog_lang)
# print(dev1.salary)

# manager1 = Manager('Jamie', 'Lanister', 3000, [dev1,dev3])
# manager1.show_emps()
# manager1.add_emps(dev2)
# print(f'Manager {manager1.get_full_name()} has {manager1.show_emps()} developers. His salary is {manager1.salary}$')
# #-------------------------------------------------------------------------------------------------
# class Post:
#     def __init__(self, user)->None:
#         self.user = user
#         self.posts = []
#         self.id = 0
#     #CRUD
#     def create_post(self, title, body, image):
#         self.id += 1
#         post = dict(id = self.id, title=title, body=body, image=image)
#         self.posts.append(post)
#         return {'status': 201, 'msg': 'successfully created'}
    
#     def retrieve_post(self, post_id):
#         for post in self.posts:
#             if post.get('id') == post_id:
#                 return post 
#         return {'status': 404, 'msg': 'Not found'}

#     def update_post(self,post_id, **kwargs):
#         for post in self.posts:
#             if post.get('id') == post_id:
#                 post.update(kwargs)
#                 return {'status': 200, 'msg': 'Updated'}
#         return {'status': 404, 'msg': 'Not found'}

#     def delete_post(self, post_id):
#         for post in self.posts:
#             if post.get('id') == post_id:
#                 self.posts.pop(self.posts.index(post))
#                 return {'status':200, 'msg': 'removed'}
#         return {'status': 404, 'msg': 'not found'}

# acc1 = Post('JohnSnow')
# acc1.create_post('Good news', 'My sister Sansa gave birth to a girl!', 'https://link.jpg')
# acc1.create_post('Walking', 'The weather is soo good', 'https://link.jpg')
# acc1.create_post('Having fun!', 'Going to Turkey to have some fun!', 'https://link.jpg')
# # print(acc1.posts)
# print(acc1.retrieve_post(1))
# print(acc1.update_post(2, title='Walking updated', body='Having a walk at 9p.m', image='https://link.jpg'))
# print(acc1.retrieve_post(2))
# print(acc1.delete_post(2))
# print(acc1.posts)
#---------------------------------------------------------------------------------------------------
# from abc import ABC, abstractclassmethod
# class ChessPiece(ABC):
#     name = 'piece'
#     def show_name(self):
#         print(f'Hello I am {self.name}')

#     @abstractclassmethod
#     def move(self):
#         pass
# class Queen(ChessPiece):
#     name = 'Queen'
#     def move(self):
#         print('Wherever she wants')
# class Pawn(ChessPiece):
#     name = 'Pawn'
#     def move(self):
#         print('One step forward')
# q = Queen()
# p = Pawn()
# q.show_name()
# p.show_name()
# q.move()
# p.move()