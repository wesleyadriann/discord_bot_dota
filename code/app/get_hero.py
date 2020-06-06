
# -*- coding: utf-8 -*-

import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.selector import Selector

from configuration import Configuration
from logger import create_logger

config = Configuration()
logger = create_logger('GET_HERO')

class Get_Hero(scrapy.Spider):
    def __init__(self, **kwargs):
        self.__hero = {"name": kwargs.get('hero_name')}
        config.configure_hero_counters_full(self.__hero['name'])
        super().__init__(name='hero', start_urls=[config.HERO_COUNTERS_FULL])

    def parse(self, response):
        handicaps, benefits = response.css('.counter-outline').extract()
        list_heroes_handicaps = Selector(text=handicaps).xpath('//tr/td/@data-value').extract()
        list_heroes_benefits = Selector(text=benefits).xpath('//tr/td/@data-value').extract()
        heroes_handicaps = []
        heroes_benefits = []
        for i in range(0, len(heroes_benefits), 4):
            heroes_handicaps.append({
                'name': list_heroes_benefits[i],
                'value': list_heroes_benefits[i+2],
            })
            heroes_benefits.append({
                'name': list_heroes_handicaps[i],
                'value': list_heroes_handicaps[i+2],
            })

        self.__hero = {
            **self.__hero,
            'handicaps': heroes_handicaps,
            'benefits': heroes_benefits,
        }
        logger.info(self.__hero)

    def get_data(self):
        return self.__hero


def run(hero_name):
    logger.info('RUNNING')
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
    })

    # try:
    crawl = process.create_crawler(Get_Hero)
    process.crawl(crawl, hero_name=hero_name)

    process.start()
    # except Exception as error:
    #     logger.error(f'\n\n\n{error}\n\n\n')

    hero = crawl.spider.get_data()

    return hero
