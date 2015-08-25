import json

from scrapy.exporters import JsonLinesItemExporter


class SchoolWriter(object):
    def __init__(self):
        self.file = open('schools.jl', 'wb')

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + '/n'
        self.file.write(line)
        return item

    def __del__(self):
        self.file.close()
