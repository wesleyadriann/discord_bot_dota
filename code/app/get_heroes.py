
# -*- coding: utf-8 -*-

import scrapy
from scrapy.crawler import CrawlerProcess

from configuration import Configuration
from logger import create_logger

config = Configuration()
logger = create_logger('GET_HEROES')

class Get_Heroes(scrapy.Spider):
    name = 'heroes'
    start_urls = [config.HEROES]

    def parse(self, response):
        names = response.css('.name').xpath('text()').extract()
        heroes = open('heroes.txt', 'w')
        heroes.write('\n'.join(names))
        heroes.close()


def run():
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
    })
    process.crawl(Get_Heroes)
    process.start()

    heroes_file = open('heroes.txt', 'r')
    heroes = heroes_file.read()
    heroes_file.close()
    return heroes
