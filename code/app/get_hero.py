
# -*- coding: utf-8 -*-

import scrapy
from scrapy.crawler import CrawlerProcess

from configuration import Configuration
from logger import create_logger

config = Configuration()
logger = create_logger('GET_HERO')

class Get_Hero(scrapy.Spider):
    def __init__(self, **kwargs):
        hero_name = kwargs.get('hero_name')
        config.configure_hero_counters_full(hero_name)

        self.__hero = "init"
        super().__init__(name='hero', start_urls=[config.HERO_COUNTERS_FULL])

    def parse(self, response):
        # names = response.css('.name').xpath('text()').extract()
        names = response.css('.counter-outline').extract()
        self.hero = "exec"

    def get_data(self):
        return self.__hero


def run(hero_name):
    logger.info('RUNNING')
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
    })

    crawl = process.create_crawler(Get_Hero)
    process.crawl(crawl, hero_name=hero_name)
    process.start()

    hero = crawl.spider.hero

    return hero
