from scrapy.item import Item,Field


class ProjectItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Author=Field()
    Quotes=Field()
    Tags=Field()

