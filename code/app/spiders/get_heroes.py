
# -*- coding: utf-8 -*-

import scrapy
from scrapy.crawler import CrawlerProcess

import runner
from configuration.configuration import Configuration
from configuration.logger import create_logger

config = Configuration()
logger = create_logger('GET_HEROES')

class Get_Heroes(scrapy.Spider):
    def __init__(self):
        self.__heroes = ""
        super().__init__(name='heroes', start_urls=[config.HEROES])

    def parse(self, response):
        names = response.css('.name').xpath('text()').extract()
        self.__heroes = '\n'.join(names)
        logger.info('Sucess parse')

    def get_data(self):
        return self.__heroes


def run():
    data = runner.run(Get_Heroes)
    return data
