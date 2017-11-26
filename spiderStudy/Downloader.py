import requests
import lxml.html
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urlsplit
from datetime import datetime, timedelta
from time import sleep
from time import sleep

class Downloader(object):
    def __init__(self, delay = 5,user_sgent = 'wswp', cache = None):
            # 设置user-agent 等基础数据
            self.user_sgent = user_sgent
            self.cache = cache
            self.throttle = Throttle(delay)
    
    def __call__(self, url):
        result = None
        #检查是否允许缓存,并获取缓存的结果
        if self.cache:
                result = self.cache[url]
        #若html文件没有被缓存过
        if result is None:
            #检查当前url是否在指定时间内被抓取过，如果是，则停留指定时间-（当前时间-上次抓取时间）
            self.throttle.wait(url)
            headers = {
                'user-agent':self.user_sgent
            }
            result = self.download(url, headers)
            #将爬去的结果添加到缓存
            if self.cache:
                self.cache[url] = result
            return result['html']

    def download(self, url, headers):
        #下载指定url
        rep = requests.get(url = url, headers = headers or {})
        html = rep.text
        code = rep.status_code
        #返回爬去到的html内容和状态码
        return {
    'html':html,
    'code':code
    }

class Throttle(object):
    def __init__(self, delay):
        self.delay = delay
        self.domains = {}
    
    def wait(self, url):
        #或者爬去网站的domain
        domain = urlparse(url).netloc
        #获取上一次爬取该domain的时间，并且返回需要等待的时间
        lasted_accessed = self.domains.get(domain)
        if self.delay and lasted_accessed is not None:
            sleep_secs = self.delay - (datetime.now() - lasted_accessed).seconds
            if sleep_secs > 0:
                sleep(sleep_secs)
        self.domains[domain] = datetime.now()
