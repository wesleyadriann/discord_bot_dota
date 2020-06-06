
# -*- coding: utf-8 -*-

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from logger import create_logger

logger = create_logger('RUNNER')
process = CrawlerProcess(get_project_settings())

def run(spider, **kwargs):
    logger.info('RUNNING')

    crawl = process.create_crawler(spider)
    process.crawl(crawl, **kwargs)
    process.start()

    data = crawl.spider.get_data()
    logger.info(data)

    return data
