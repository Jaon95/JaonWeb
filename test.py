import string
from spiderStudy import Downloader
import json

template_url = 'http://example.webscraping.com/places/ajax/search.json?&search_term={}&page_size=10&page={}'

countries = set()
D = Downloader.Downloader()

for letter in string.ascii_letters:
    page = 0
    while True:
        html = D(template_url.format(page, letter))
        try:
            ajax = json.loads(html)
        except Exception as identifier:
            ajax = None
        else:
            for record in ajax['records']:
                countries.add(record['country'])
        page += 1
        if ajax is None or page >= ajax['num_pages']:
            break

open('countries.txt', 'w').write('\n'.join(sorted(countries)))
