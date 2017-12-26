import lxml


class Downloader(object):
    def __init__(self, session, headers):
        self.session = session
        self.session.headers.update(headers)
    
    def __call__(self, url, method, data =None):
        if method == 'POST':
            return self.session.post(url, data=data)
        if method == 'GET':
            return self.session.get(url)

def handlerKNKC(httpsession, resp):
    html = resp.text
    htmltree = lxml.html.fromstring(html)
    #sava the data
    #code...

    #返回
    return []