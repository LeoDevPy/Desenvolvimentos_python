#from pymongo import MongoClient 

from pymongo import MongoClient 


conn = MongoClient('localhost', 27017)


db = conn.cadastrodb

collection = db.cadastrodb

import datetime 

post1 = {"codigo": "ID-998775",
         "prod_name": "Geladeira",
         "marcas": ['brastemp','consul','eletrolux'],
         "data_cadastros": datetime.datetime.utcnow()}

collection = db.posts 

post_id = collection.insert_one(post1)

post_id.inserted_id 

print(post_id)

post2 = {"codigo": "ID-2209807",
         "prod_name": "Televisor",
         "marcas": ['samsung','panasonic','tcl'],
         "data_cadastros": datetime.datetime.utcnow()}

collection = db.posts 

post_id = collection.insert_one(post2).inserted_id

collection.find_one({"prod_name":"Televisor"})

for post in collection.find():
    print(post)
    
db.name

print(db.collection_names())

