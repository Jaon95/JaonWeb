from pymongo import MongoClient
import datetime

client = MongoClient('localhost', 27017)
db = client.tes_database
collection = db.test_collection

post = {
    'author':'Jaon95',
    'title':'first novel',
    'content':'this is a post',
    'time':datetime.datetime.utcnow()
}

posts = db.posts
post_id = posts.insert_one(post).inserted_id
print(post_id)