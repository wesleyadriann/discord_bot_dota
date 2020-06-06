
# -*- coding: utf-8 -*-

import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.selector import Selector
from scrapy.utils.project import get_project_settings

from configuration import Configuration
from logger import create_logger

config = Configuration()
logger = create_logger('GET_HERO')

class Get_Hero(scrapy.Spider):
    def __init__(self, **kwargs):
        self.__hero = {'name': kwargs.get('hero_name')}
        config.configure_hero_counters_full(self.__hero['name'])
        super().__init__(name='hero', start_urls=[config.HERO_COUNTERS_FULL])

    def parse(self, response):
        handicaps, benefits = response.css('.counter-outline').extract()
        list_heroes_benefits = Selector(text=benefits).xpath('//tr/td/@data-value').extract()
        list_heroes_handicaps = Selector(text=handicaps).xpath('//tr/td/@data-value').extract()
        heroes_benefits = [list_heroes_benefits[i] for i in range(0, len(list_heroes_benefits), 4)]
        heroes_handicaps = [list_heroes_handicaps[i] for i in range(0, len(list_heroes_benefits), 4)]

        self.__hero = {
            **self.__hero,
            'handicaps': heroes_handicaps,
            'benefits': heroes_benefits,
        }

        return

    def get_data(self):
        return self.__hero


async def run(hero_name):
    logger.info('RUNNING')
    process = CrawlerProcess(get_project_settings())

    crawl = process.create_crawler(Get_Hero)
    process.crawl(crawl, hero_name=hero_name)
    process.start()


    hero = crawl.spider.get_data()
    logger.info(hero)

    return hero


