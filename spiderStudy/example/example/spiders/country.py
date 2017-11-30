# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from example.items import ExampleItem

class CountrySpider(CrawlSpider):
    name = 'country'
    allowed_domains = ['exampla.webscraping.com']
    start_urls = ['http://example.webscraping.com']

    rules = (
        Rule(LinkExtractor(allow='/index/'), follow=True),
        Rule(LinkExtractor(allow='/view/'), callback='parse_item', follow=True)
    )

    def parse_item(self, response):
        i = ExampleItem()
        name_css = '#places_country__row > td.w2p_fw::text'
        i['name'] = response.css(name_css).extract()
        pop_css = '#places_population__row > td.w2p_fw:text'
        i['population'] = response.css(pop_css).extract()
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i
