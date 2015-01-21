# -*- coding: utf-8 -*-

# Scrapy settings for getSis project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'getSis'

SPIDER_MODULES = ['getSis.spiders']
NEWSPIDER_MODULE = 'getSis.spiders'

'''
DOWNLOADER_MIDDLEWARES = {
    #'scraper.random_user_agent.RandomUserAgentMiddleware': 400,
    #'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware':None,
    #'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 110,
    #'getSis.middlewares.Proxyware.ProxyMiddleware': 100,
    #'getSis.middlewares.google_cache.GoogleCacheMiddleware': 50,
}
'''
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'getSis (+http://www.yourdomain.com)'
