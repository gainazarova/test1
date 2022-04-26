import requests
from bs4 import BeautifulSoup

url = 'https://www.kivano.kg/mobilnye-telefony'

def get_html(url:str)-> str:
    response = requests.get(url)
    return response.text

def get_data(html:str)-> None:
    soup = BeautifulSoup(html,'lxml')
    # print(soup)
    catalog = soup.find_all('div', class_='item product_listbox oh')
    # print(catalog)
    for info in catalog:
        model = info.find('div', class_='listbox_title oh').text
        # print(model)
        price = info.find('div', class_='listbox_price text-center').find('strong').text
        # print(price)
        img_link = info.find('img').get('src')
        img_link1 = 'https://www.kivano.kg'+img_link
        print(img_link1)
        
        data = {
            'model': model,
            'price': price,
            'img_link': img_link1
        }
        write_to_csv(data)

def write_to_csv(data):
    import csv
    with open('phones.csv', 'a') as file:
        fieldnames = [ 'model', 'price','img_link']
        writer = csv.DictWriter(file,fieldnames)
        writer.writerow({
            'model': data.get('model'),
            'price': data.get('price'),
            'img_link': data.get('img_link')
        })


get_data(get_html(url))
