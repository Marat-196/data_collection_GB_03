from pymongo import MongoClient
from pprint import pprint
from pymongo.errors import *
import json

client = MongoClient('localhost', 27017)
db = client['books']

books = db.books
duplicates = db.duplicates

# with open('books.json', 'r') as f:
#     data = json.load(f)
#
# for book in data:
#     try:
#         books.insert_one(book)
#     except DuplicateKeyError as e:
#         duplicates.insert_one(e)


# Вывод записи со стоимостью 51.77
# for doc in books.find({"price": 51.77}):
#     pprint(doc)


# Вывод записи у которой стоимость 53,74 И наличие 20 шт
# for doc in books.find({"price": 53.74, "Availability": 20}):
#     pprint(doc)


# Вывод записи у которой стоимость от 20 до 30 И наличие больше 15 шт, без вывода метрики описания, и в отсортированные по имени
# for doc in books.find({'$and': [{'price': {'$gt': 20, '$lt': 30}}, {'Availability': {'$gt': 15}}]}, {'Description': 0}).sort('name'):
#     pprint(doc)

# Вывод записей в которых наименование книги начинается с буквы S, при этом отключение отображения поля -Id, и сортировка записей по имени
# for doc in books.find({'name': {'$regex': 'S. '}}, {'_id': 0}).sort('name'):
#     print(doc)




