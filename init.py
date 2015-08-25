import json

import scrapy
from scrapy.crawler import CrawlerProcess

from eduStats.spiders.eduspider import EduSpider

process = CrawlerProcess()
process.crawl(EduSpider)
process.start()
