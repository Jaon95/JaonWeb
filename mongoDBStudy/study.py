from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client.cache


#下面是简单的插入语句
db.webpage.insert_one({
    'url':'i am url',
    'html':'<html></html>'
})

#下面是简单的更新语句
entry = db.webpage.update({
    '_id':'http://www.baidu.com'
}, {
    '$set':{
        'html':'asdfagdasdg',
        'code':'ddafsdfa'
    }
}, upsert=True)
