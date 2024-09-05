# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import TakeFirst, MapCompose


class ReportscraperItem(scrapy.Item):
    
    title = scrapy.Field(
        input_processor = MapCompose(),
        output_processor = TakeFirst()
    )
    
    file_urls = scrapy.Field()
    
    files = scrapy.Field()
