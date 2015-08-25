import scrapy


class SiteData(scrapy.Item):
    # Summary Fields
    url = scrapy.Field()
    name = scrapy.Field()
    domain = scrapy.Field()
    title = scrapy.Field()
    # CSS fields
    css_paths = scrapy.Field()
    css_files = scrapy.Field()
    # JS fields
    js_paths = scrapy.Field()
    js_files = scrapy.Field()
    # Tag fields
    tagcount = scrapy.Field()
    nonvoidcount = scrapy.Field()
    topnest = scrapy.Field()
