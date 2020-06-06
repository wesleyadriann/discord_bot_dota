
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
        hero_name = kwargs.get('hero_name')
        config.configure_hero_counters_full(hero_name)
        self.__hero = "init"
        super().__init__(name='hero', start_urls=[config.HERO_COUNTERS_FULL])

    def parse(self, response):
        handicaps, benefits = response.css('.counter-outline').extract()
        list_heroes_handicaps = Selector(text=handicaps).xpath('//tr/td/@data-value').extract()
        list_heroes_benefits = Selector(text=benefits).xpath('//tr/td/@data-value').extract()
        logger.info(list_heroes_benefits)
        logger.info(list_heroes_handicaps)
        heroes_benefits = []
        # heroes_
        for i in range(0, len(heroes_benefits), 4):
            heroes_benefits.append({
                'name': list_heroes_benefits[i],
                'value': list_heroes[i+2]
            })

        self.__hero = "exec"

    def get_data(self):
        return self.__hero


async def run(hero_name):
    logger.info('RUNNING')
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
    })

    crawl = process.create_crawler(Get_Hero)
    process.crawl(crawl, hero_name=hero_name)
    process.start()

    hero = crawl.spider.get_data()

    return hero
