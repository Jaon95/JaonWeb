
import Downloader

def link_crawler(seed_url,  delay=5,  max_urls=-1, user_agent='wswp', scrape_callback=None, cache=None):
    crawl_queue = [seed_url]

    num_urls = 0

    #初始化downloader 
    D = Downloader.Downloader(delay = delay,user_sgent = user_agent, cache = cache)

    while crawl_queue:
        url = crawl_queue.pop()

        html = D(url)
        links = []

        if scrape_callback:
            links.extend(scrape_callback(url, html) or [])
        
        if num_urls <= max_urls:
            for link in links:
                crawl_queue.append(link)
                num_urls += 1
                if num_urls > max_urls:break
        
