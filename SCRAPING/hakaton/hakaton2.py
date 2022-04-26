
import requests
from bs4 import BeautifulSoup
import csv

BASE_URL = 'https://www.mashina.kg/search/all/'

def get_html(url:str)-> str:
    response = requests.get(url)
    return response.text

def get_data(html:str)-> None:
    soup = BeautifulSoup(html, 'lxml')
    model = soup.find_all('div', class_='block title')
    for i in model:
        model1 = i.text

    price = soup.find_all('div', class_='block price')
    for i in price:
        price1 = i.text
    
    charac = soup.find_all('div', class_='block info-wrapper item-info-wrapper')
    for i in charac:
        characteristic = i.text

    # image = soup.find_all('div', class_= 'image-wrap')
    # for i in image:
    #     a = 'https://www.mashina.kg/'
    #     img_link = a + i.get('src')
    #     print(img_link)
        
        data = {
        'name': model1,
        'price': price1,
        'description': characteristic
        # 'img_link': img_link
        }
        write_to_csv(data)   


def write_to_csv(data):
  with open('mashinakg.csv', 'a') as file:
    fieldnames = ['name','price','description']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writerow(data['name'],data['price'],data['description'])
get_data(get_html(BASE_URL))




