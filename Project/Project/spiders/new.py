# -*- coding: utf-8 -*-
import scrapy
from Project.items import ProjectItem
import re


class NewSpider(scrapy.Spider):
    name = 'new'
    allowed_domains = ['goodreads.com']
    start_urls = ['https://www.goodreads.com/quotes/tag/life']

    def parse(self, response):
        for quote in response.css('div.quoteDetails'):

            item = ProjectItem()
            substring1 = quote.css("div.quoteText::text").get()
            item['Quotes'] =re.sub('[^A-Za-z0-9]+',' ',substring1)
            substring2= quote.css("span.authorOrTitle::text").get()
            item['Author'] = re.sub('[^A-Za-z0-9]+', ' ', substring2)
            item['Tags'] = quote.css("div.greyText.smallText.left a::text").getall()
            yield item

