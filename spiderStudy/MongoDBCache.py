from urllib.parse import urlsplit
import re
import os
import pickle
from datetime import datetime, timedelta
import zlib
from pymongo import MongoClient
import time

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
            return record['result']
        else:
            return None

    
    def __setitem__(self, url, result):
        self.db.webpages.update({
            '_id':url
        }, {
            '$set':{
                'result':result,
                'timestamp':datetime.utcnow()
            }
        }, upsert=True)

if __name__ == '__main__':
    cache = MongoCache(expires = timedelta())
    result = {
        'html':'....'
    }
    url = 'http://www.baidu.com'
    time.sleep(70)
    cache[url] = result
    print(cache[url])
