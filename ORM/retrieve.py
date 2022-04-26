import peewee

from models import Category, Product

def find_all_categories():
    return Category.select()

def find_all_products():
    return Product.select()

categories = find_all_categories()
products = find_all_products()

print('Категории в бд:')
for x in categories:
    print(x.name)

print('Все продукты в бд:')
for x in products:
    print(f'title: {x.title}, price: {x.price}, category: {x.category}')