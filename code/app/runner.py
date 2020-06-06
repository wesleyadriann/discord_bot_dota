
# -*- coding: utf-8 -*-

from multiprocessing import Process, Queue
from scrapy.crawler import CrawlerProcess, CrawlerRunner
from scrapy.utils.project import get_project_settings
from twisted.internet import reactor

from logger import create_logger

logger = create_logger('RUNNER')

def run(spider, **kwargs):
    logger.info('RUNNING')

    def f(queue):
        process = CrawlerProcess(get_project_settings())
        crawl = process.create_crawler(spider)
        process.crawl(crawl, **kwargs)
        process.start()
        data = crawl.spider.get_data()
        queue.put(data)

    queue = Queue()
    process = Process(target=f, args=(queue,))
    process.start()
    data = queue.get()
    process.join()

    return data
