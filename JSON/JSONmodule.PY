
# JSON(JAVA SCRIPT OBJECT NOTATION)- единный формат для хранения и передачи данных между компьютерами, сервисами, приложениями и языками программирования через сеть(интернет).

# <filename>.json
# JS object == Python Dict == JSON
# JAVA -> PYTHON = JSON/XML 

# JSON помогает доставить инфу из серверной части в клиентскую, в виде словаря(ключ:значение)
# серверная часть (back end) -> (front end)клиентская часть
# {
#     'id':
#     'author':'John',
#     'posts':[...]
# } - это Json, наша задача перевести его в Python Dict. 

# !!!
# JS object == {}
# Py dict =={}
# JSON == {}

# Процессы сериализации данных и десериализации:

# Сериализация данных-перевод Python dict в JSON формат (либо сохранить в файле либо просто как текстовые данные).  
# dump-запись данных в JSON файл
# dumps-запись данных в JSON в текстовом формате

# Десериализация данных- перевод из JSON в Python dict.
# load - из файла JSON данные и переводим в dict.
# loads - из JSONа в текстовом формате переводим данные в dict.

#----------------------------------------------------------------------------------------------------

# """Процесс десериализации"""
# import json
# from urllib.request import urlopen 

# data = urlopen('https://randomuser.me/api/')
# # print(data)
# generate_to_dict = json.load(data)
# print(generate_to_dict)
# print(type(generate_to_dict))
# print(generate_to_dict['results'])
# print(generate_to_dict.keys())

# with open('downAPI.json','w') as file:
#     file.write(str(generate_to_dict))
    
#Процесс сериализации:
# import json
# data = {
#     'name': 'John',
#     'last_name': 'Snow',
#     'status': True
# }
# with open('downAPI.json', 'w') as file:
#     json.dump(data, file)

# import json
# data = {
#     'name': 'John',
#     'last_name': 'Snow',
#     'status': True
# }

# string = json.dumps(data)
# print(string)
# print(type(string))
# py_dict = json.loads(string)
# print(py_dict)
# print(type(py_dict))

# from urllib.request import urlopen
# import json 

# data = urlopen('https://randomuser.me/api/')
# py_dict = json.load(data)
# print(type(py_dict))

# with open('downAPI.json', 'a') as file:
#     json.dump(py_dict, file)

# nums = [2,2,1]
# for i in nums:
#     if nums.count(i) == 1:
#         print(i)

# nums = [4,1,2,1,2]
# for i in nums:
#     if nums.count(i) == 1:
#         print(i)













