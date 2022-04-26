
import requests
from bs4 import BeautifulSoup

import datetime

BASE_URL = "https://cars.kg/offers"

def get_html(url:str)-> str:
    """
    Получает html код определенной страницы 
    """
    response = requests.get(url)
    return response.text

def get_data(html:str)-> None:
    """
    Это функция парсер получает все данные 
    """
    soup = BeautifulSoup(html,'lxml')
    # print(soup)
    catalog = soup.find('div',class_='catalog-list')
    # print(catalog)
    cars = catalog.find_all('a',class_='catalog-list-item')
    # print(cars[0])
    # car1 = cars[0].find('span',class_ = 'catalog-item-caption')
    # print(car1.text.strip())
    for car in cars:
        title = car.find('span', class_='catalog-item-caption').text.strip()

        
        mileage = car.find('span', class_='catalog-item-mileage').text
        if not mileage:
            mileage = "Пробега нет"

        price = car.find('span', class_='catalog-item-price').text.strip()
        try:
            img = car.find('img', class_='catalog-item-cover-img').get('src')
        except:
            img='Картины нет'
        data = {
            'title': title,
            'mileage': mileage,
            'price': price,
            'img': img
        }

        write_to_csv(data)


        # print(f'Название {title}, км: {mileage} , Цена:{price} , Фотка {img}')


#get_data(get_html(BASE_URL))

def write_to_csv(data: dict)-> None:
    """Функция для записи данных в csv файл"""
    import csv
    with open('cars.csv', 'a') as file:
        fieldnames = ['Марка машины', 'Пробег','Цена', 'Фото']
        writer = csv.DictWriter(file, fieldnames)
        writer.writerow({
            'Марка машины': data.get('title'),
            'Пробег': data.get('mileage'),
            'Цена': data.get('price'),
            'Фото': data.get('img')
        })


i = 1
k = 20
start = datetime.datetime.now()
while True:
    BASE_URL = f'https://cars.kg/offers/{i}'

    html = get_html(BASE_URL)
    catalog = BeautifulSoup(html, 'lxml').find('div', class_='catalog-list')

    if i > 5:
        break
    # if not catalog:
    #     break

    get_data(html)
    i += 1
    k += 20
    #print(f'страница: {i}, Машина {k}')
end = datetime.datetime.now()
print(end - start)





