# -*- coding: utf-8 -*-
# Scrapy settings for meizi_spider project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'meizi_spider'

SPIDER_MODULES = ['meizi_spider.spiders']
NEWSPIDER_MODULE = 'meizi_spider.spiders'

# 禁用Cookie
COOKIES_ENABLED = True
COOKIES_DEBUG = True

# 设置请求间隔
DOWNLOAD_DELAY = 2

# 设置Pipeline
ITEM_PIPELINES = {
    'meizi_spider.pipelines.MeiziPipeline': 300,
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'meizi_spider (+http://www.yourdomain.com)'
