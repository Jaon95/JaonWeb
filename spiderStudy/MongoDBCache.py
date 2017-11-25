from urllib.parse import urlsplit
import re
import pickle
from datetime import datetime, timedelta
import zlib
from pymongo import MongoClient
import time
import zlib

class MongoCache(object):
    def __init__(self, client = None, expires = timedelta(days = 30)):
        self.client = MongoClient() if client is None else client
        self.db = self.client.cache
        self.db.webpages.create_index('timestamp', expireAfterSeconds = expires.total_seconds())

    def __getitem__(self, url):
        record = self.db.webpages.find_one({
            '_id':url
        })
        if record:
            return pickle.loads(zlib.decompress(record['result']))
        else:
            return None

    
    def __setitem__(self, url, result):
        self.db.webpages.update({
            '_id':url
        }, {
            '$set':{
                'result':zlib.compress(pickle.dumps(result)),
                'timestamp':datetime.utcnow()
            }
        }, upsert=True)

if __name__ == '__main__':
    cache = MongoCache(expires = timedelta())
    result = {
        'html':'....'
    }
    url = 'http://www.baidu.com'
    cache[url] = result
    print(cache[url])
