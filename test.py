from pymongo import MongoClient
import datetime
import csv
from zipfile import ZipFile

with ZipFile('F://top-1million-sites.csv.zip','r') as zf:
    cvs_filename = zf.namelist()[0]
    for _, website in csv.reader(zf.open(cvs_filename)):
        print(website)