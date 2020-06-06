
# -*- coding: utf-8 -*-

import scrapy
from scrapy.crawler import CrawlerProcess

from configuration import Configuration
from logger import create_logger

config = Configuration()
logger = create_logger('GET_HEROES')

class Get_Heroes(scrapy.Spider):
    def __init__(self):
        self.__heroes = ""
        super().__init__(name='heroes', start_urls=[config.HEROES])

    def parse(self, response):
        names = response.css('.name').xpath('text()').extract()
        self.__heroes = '\n'.join(names)

    def get_data(self):
        return self.__heroes


def run():
    logger.info('RUNNING')
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
    })

    crawl = process.create_crawler(Get_Heroes)
    process.crawl(crawl)
    process.start()

    heroes = crawl.spider.get_data()
    return heroes
