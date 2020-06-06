
# -*- coding: utf-8 -*-

import scrapy

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


