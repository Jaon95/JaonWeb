import requests
import lxml.html
from PIL import Image
from io import BytesIO
import cssselect
import base64
import pytesseract
import string

def parseForm(html):
    tree = lxml.html.fromstring(html)
    data = {}
    for item in tree.cssselect('form input'):
        if item.get('name'):
            data[item.get('name')] = item.get('value')
    return data

def get_img(html):
    tree = lxml.html.fromstring(html)
    img_data = tree.cssselect('div#recaptcha img')[0].get('src')
    img_data = img_data.partition(',')[-1]
    binary_img_data = base64.b64decode(img_data)
    file_like = BytesIO(binary_img_data)
    img = Image.open(file_like)
    return img

def ocr(img):
    gray = img.convert('L')
    bw = gray.point(lambda x: 0 if x <1 else 255, '1')
    bw.save('test.png')
    return 'sscii_word'

if __name__ == '__main__':
    # html = requests.get('http://example.webscraping.com/places/default/user/register').text
    # img = get_img(html)
    # data = parseForm(html)
    session = requests.Session()
    html = session.get('http://example.webscraping.com/places/default/user/register').text
    data = parseForm(html)
    img = get_img(html)
    print(data)
    print(ocr(img))