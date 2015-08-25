""" eduStats/spiders/edu_spider.py
Defines class "eduSpider" for scraping ".edu" websites
"""

import scrapy
from scrapy.exporters import JsonLinesItemExporter

from eduStats.items import SiteData
from eduStats.tagcounter import TagCounter


class EduSpider(scrapy.Spider):
    """ Used to scrape .edu websites for web technology statistics """
    name = 'edu'

    def __init__(self):
        scrapy.Spider.__init__(self)

        baseurl = "https://domaintyper.com/top-websites/most-popular-websites-with-edu-domain/page/"
        self.start_urls = [baseurl + str(i) for i in xrange(1, 3)]
        self.domain = 'domaintyper.com'
        self.exporter = JsonLinesItemExporter(open('schools.jl', 'wb+'))

    # def parse(self, response):
    #     self.exporter.start_exporting()
    #     urls = [url.encode('utf-8') for url in response.css('.wsTR > td:nth-child(2)').xpath('text()').extract()]
    #     for url in urls:
    #         fullurl = 'http://www.' + url + '/'
    #         yield scrapy.Request(fullurl, callback=self.parse_edu_site)
    #
    # def parse_edu_site(self, response):
    def parse(self, response):
        data = SiteData()
        tc = TagCounter()

        # Fill summary fields
        data['domain'] = '.'.join(response.url.split('/')[2].split('.')[-2:])
        data['name'] = data['domain'].split('.')[0]
        data['title'] = response.xpath('//title/text()').extract()[0].encode('utf-8')

        # Fill CSS fields
        data['css_paths'] = [stylesheet.encode('utf-8') for stylesheet in response.xpath('//link[@rel="stylesheet"]/@href').extract()]
        data['css_files'] = [stylesheet.split('/')[-1] for stylesheet in data['css_paths']]

        # Fill JS fields
        data['js_paths'] = [script.encode('utf-8') for script in response.xpath('//script/@src').extract()]
        data['js_files'] = [script.split('/')[-1] for script in data['js_paths']]

        # Fill tag fields
        tc.feed(response.body)
        data['tagcount'] = tc.tagcount
        data['nonvoidcount'] = tc.nonvoid_tagcount
        data['topnest'] = tc.topnest

        self.exporter.export_item(data)
        yield data

    def __del__(self):
        scrapy.Spider.__del__(self)
        self.exporter.finish_exporting()
