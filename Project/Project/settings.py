BOT_NAME = 'Project'

SPIDER_MODULES = ['Project.spiders']
NEWSPIDER_MODULE = 'Project.spiders'
ITEM_PIPELINES = {'Project.pipelines.ProjectPipeline':300}

MONGODB_SERVER = "localhost"
MONGODB_PORT = 27017
MONGODB_DB = "goodreads"
MONGODB_COLLECTION = 'quotes'
