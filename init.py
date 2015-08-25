import json

import scrapy
from scrapy.crawler import CrawlerProcess

from eduStats.spiders.eduspider import EduSpider

process = CrawlerProcess()
process.crawl(EduSpider)
process.start()


# Code saved because useful for webpage access later
# schools = {}
# with open('schools.jl', 'r') as f:
#     for line in f.readlines():
#         school = json.loads(line)
#         schools[school['name']] = school
