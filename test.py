from pymongo import MongoClient
import datetime
import csv
from zipfile import ZipFile
import io
from spiderStudy import LinkCrawler
from spiderStudy import MongoDBCache

with ZipFile('F://top-1million-sites.csv.zip') as zf:
    cvs_filename = zf.namelist()[0]
    csv_reader = csv.reader(zf.open(cvs_filename))
    f = io.TextIOWrapper(zf.open(cvs_filename))
    csv_reader = csv.reader(f)
    urls = []
    nums = 0
    for _, website in csv_reader:
        if nums >= 50: break
        urls.append('https://www.'+website)
        nums += 1
    LinkCrawler.link_crawler(urls, max_urls = 50,cache = MongoDBCache.MongoCache())
    
