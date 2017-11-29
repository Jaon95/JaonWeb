import lxml.html
import select

def parseForm(html):
    tree = lxml.html.fromstring(html)
    data = {}
    for item in tree.cssselect('form input'):
        if item.get('name'):
            data[item.get('name')] = item.get('value')
    return data
