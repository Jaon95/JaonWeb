import requests
from spiderStudy import Downloader
import lxml.html
import cssselect

EMAIL = 'jasonlmh0314@outlook.com'
PASSWORD = 'webscraping0314'
def parseForm(html):
    tree = lxml.html.fromstring(html)
    data = {}
    for item in tree.cssselect('form input'):
        if item.get('name'):
            data[item.get('name')] = item.get('value')
    return data

s =requests.Session()
data = parseForm(s.get('http://example.webscraping.com/places/default/user/login').text)
data['email'] = EMAIL
data['password'] = PASSWORD
for item in s.cookies.iterkeys():
    print(item +': '+s.cookies[item])
rep = s.post('http://example.webscraping.com/places/default/user/login', data = data)
# rep = s.get('http://example.webscraping.com/places/default/edit/Afghanistan-1')
# data = parseForm(rep.text)
# print(data)
for item in s.cookies.iterkeys():
    print(item +': '+s.cookies[item])
print(rep.url)
rep = s.get('http://example.webscraping.com/places/default/edit/Afghanistan-1')
data = parseForm(rep.text)
print(data)
data['population'] = int(data['population'])+1
s.post('http://example.webscraping.com/places/default/edit/Afghanistan-1', data = data)
rep = s.get('http://example.webscraping.com/places/default/edit/Afghanistan-1')
data = parseForm(rep.text)
print(data)