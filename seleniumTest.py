import urllib

from flask import Flask
from werkzeug.routing import BaseConverter

app = Flask(__name__)

class ListConverter(BaseConverter):
    def __init__(self, url_map, separator = '+'):
        super(ListConverter, self).__init__(url_map)
        self.separator = separator
    
    def to_python(self, value):
        print('---in to_python-----')
        print(value)
        return value.split(self.separator)

    def to_url(self, values):
        print('---to_url---')
        print(values)
        return self.separator.join(super(ListConverter,self).to_url(value) for value in values)

app.url_map.converters['List'] = ListConverter

@app.route('/list/<List(separator = "|"):page_nums>/')
def list2(page_nums):
    return 'Seperator: {} {} '.format('+', page_nums)

@app.route('/list/<List:page_nums>/')
def list1(page_nums):
    return 'Seperator: {} {} '.format('+', page_nums)



if __name__ == '__main__':
    app.debug = True
    app.run('127.0.0.1', 8000)
