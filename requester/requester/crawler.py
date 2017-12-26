

def link_crawl_execute(session,downlaoder,seed_url,func):
    urls = []
    urls.extend(seed_url)

    item=urls.pop()
    while item:
        resp = downlaoder(item[0])
        newUrls = func(session, resp)
        urls.extend(newUrls)
        item=urls.pop()