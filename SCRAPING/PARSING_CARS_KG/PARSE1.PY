import requests
from bs4 import BeautifulSoup

BASE_URL = 'http://www.example.com/'
def get_html(url:str)-> str:
  response = requests.get(url)
  return response.text

def get_data(html:str)-> None:

  soup = BeautifulSoup(html,'lxml')
  text = soup.find('div')
  h1 = text.find('h1')
  par = text.find('p')
  link = text.find('a')
  print(h1)
  print(par)
  print(link)
get_data(get_html(BASE_URL))
