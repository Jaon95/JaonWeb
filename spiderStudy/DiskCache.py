from urllib.parse import urlsplit
import re
import os
import pickle
from datetime import datetime, timedelta
import zlib

class DiskCache(object):
    def __init__(self, cache_dir = 'cache', expires = timedelta(days = 30)):
        self.cache_dir = cache_dir
        self.maxlength = 255
        self.expires = expires
    
    def urlToPath(self, url):
        #将url转换成目录
        net_domain = urlsplit(url)
        path = net_domain.path
        if not path:
            path = '/index.html'
        elif path.endswith('/'):
            path += 'index.html'
        file_name = net_domain.netloc + path + net_domain.query
        file_name = re.sub('[^/0-9a-zA-Z\-.,;_]', '_', file_name)
        file_name = os.path.sep.join(item[:225] for item in file_name.split('/'))
        return os.path.join(self.cache_dir, file_name)

    def __getitem__(self, url):
        #将url转化成文件地址
        path = self.urlToPath(url)
        #查看文件是否存在，如存在则读出并返回
        if os.path.exists(path):
            with open(path, 'rb') as f:
                result, save_time = pickle.loads(zlib.decompress(f.read()))
                #检查URL是否需要更新
                if self.hasExpired(save_time):
                    #raise KeyError(url +'has expired')
                    return None
                else:
                    return result
    
    def __setitem__(self, url, result):
        #将url转化成文件地址
        path = self.urlToPath(url)
        #检查文件是否存在，若不存在，则创建文件
        folder = os.path.dirname(path)
        if not os.path.exists(folder):
            os.mkdir(folder)
        #将数据以及当前时间转化
        data = pickle.dumps((result, datetime.utcnow()))
        #将下载的内容缓存至对应文件
        with open(path, 'wb') as fp:
            fp.write(zlib.compress(data))
    
    def hasExpired(self,timestamp):
        return datetime.utcnow() > timestamp + self.expires