# -*- coding: utf-8 -*-

__author__ = 'lpe234'

from twisted.internet import reactor
from scrapy.crawler import Crawler
from scrapy import log, signals
from meizi.spiders.meizi_spider import MeiziSpider
from meizi.spiders.imooc_spider import ImoocSpider
from scrapy.utils.project import get_project_settings

# spider = MeiziSpider()
spider = ImoocSpider()
settings = get_project_settings()
crawler = Crawler(settings)
crawler.signals.connect(reactor.stop, signal=signals.spider_closed)
crawler.configure()
crawler.crawl(spider)
crawler.start()
log.start(loglevel=log.DEBUG)
reactor.run() # the script will block here until the spider_closed signal was sent