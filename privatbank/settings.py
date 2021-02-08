BOT_NAME = 'privatbank'

SPIDER_MODULES = ['privatbank.spiders']
NEWSPIDER_MODULE = 'privatbank.spiders'
FEED_EXPORT_ENCODING = 'utf-8'
LOG_LEVEL = 'ERROR'
DOWNLOAD_DELAY = 0

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
	'privatbank.pipelines.PrivatbankPipeline': 100,

}