#Работа с файлами 

#указатель 
#open(<Путь до вашего файла>)

# file = open('/home/sanzhar/Desktop/ev.19/files/text/txt')-абсолютный путь 
# file = open('text.txt')-относительный путь 

# Режимы для работы с файлами
# 1. r / r+ (read) 
# 2. w / w+ (write)
# 3. a / a+ (append)
#  t (text)
#  b (binary)
#  x (создает новый файл)

# file = open('text.txt', 'r')
# data = file.read()
# data = data.split('\n')
# print(data)
# file.close()

# file = open('text.txt', 'r')
# data = file.readlines()
# print(data)
# file.close()

#Контекстный менеджер 
# with open('text.txt') as file:
#     data = file.read()
#     print(data)


# with open('text.txt', 'w') as file:
#     file.write('Hello, file was opened with ')

# ls = ['Hello world', 'My name is John', 'I am 35 years old']
# with open('text.txt','w') as file:
#     file.writelines(line + '\n' for line in ls)

# with open('/home/admins/Desktop/Files/text.txt', 'a') as file:      #абсолютный путь
#     file.write('New string')


# file.tell()-> возвращает индекс где находится указатель
# file.seek(int)-> перемещает указатель на указанный int

#----------------------------------------------------------------------------------------------------
# try:
#     from PIL import Image 
# except ImportError:
#     import Image

# import pytesseract
# import re

# def get_imei_code(image):
#     list_of_imei = []
#     string1 = pytesseract.image_to_string(image)
#     list_of_imei.append(re.findall(r'ME.\d.\s\d+',string1))
#     print(list_of_imei)
#     #print(string1)
    
#     with open('imeicode.txt', 'w') as file:
#         for x in list_of_imei[0]:
#             file.write(x)
# get_imei_code('/home/admins/Desktop/Files/imei.jpg')

# file = open('task1.txt', 'r')
# data = file.read()
# print(data)


# file = open('task3.txt','w+')
# data = file.write('1 2 3 4 5 6 7 8 9 10')
# print(data)




# file = open('task2.txt', 'r')
# data = file.read()
# print(data)

# with open('task2.txt', 'r') as file:
#     count = sum(1 for line in open('task2.txt','r'))
#     print(count)

# with open('task2.txt', 'r') as file:
#     n = [max(i) for i in file]
#     m = [min(i) for i in file]
# #print(f'max_num: {max}, min_num: {min}')
#     print(n)


# with open('task2.txt', 'r') as file:
#     mass = []
#     full_file = file.read()
#     for i in full_file.split():
#         mass.append(int(i))
# with open('task5.txt', 'w') as file2:
#     print(f'max_num:', max(mass), file=file2)
#     print(f'min_num:', min(mass), file=file2)

# with open('task2.txt', 'r') as file:
#     print(file)






