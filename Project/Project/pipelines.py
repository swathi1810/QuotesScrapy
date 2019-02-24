import pymongo
from scrapy import log
from scrapy.conf import settings
from scrapy.exceptions import DropItem

class ProjectPipeline(object):
    def __init__(self):
        connection=pymongo.MongoClient(
            settings['MONGODB_SERVER'],
            settings['MONGODB_PORT']
        )
        db=connection[settings['MONGODB_SERVER']]
        self.collection=db[settings['MONGODB_COLLECTION']]

    def process_item(self, item, spider):
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem("Missing {0}!".format(data))
        if valid:
            self.collection.insert(dict(item))
            log.msg("Quote added to MongoDB database!",
                    level=log.DEBUG, spider=spider)
        return item

