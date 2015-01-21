#coding:utf-8
'''
#coding:utf-8
import scrapy
import urllib
import re

from getSis.items import GetsisItem

num = 0
item = []
class getSisSpider(scrapy.Spider):
    name = "getSis"
    #allowed_domains = ["51job.com"]
    start_urls = [
        #"http://38.103.161.187/forum/forumdisplay.php?fid=25"
        "http://38.103.161.187/forum/forum-25-1.html",
        #"http://38.103.161.187/forum/forum-25-2.html"

    ]
    page = raw_input("input something?")  #输入你要找的页数
    for page in xrange(2,(int(page)+1)):
        start_urls.append("http://38.103.161.187/forum/forum-25-%d.html"%page)

    def parse(self, response):
        if response.url == "http://38.103.161.187/forum/forum-25-1.html": #response.url 才是对应的url地址
            for sel in response.xpath('//*[@id="wrapper"]/div[1]/div[7]/form[@method]/table/table/table/table/tbody/tr/th/span[@id]'):
                name =sel.xpath('a/text()').extract()
                item.append(name)
                link = sel.xpath('a/@href').extract()
                linkTure = 'http://38.103.161.187/forum/'+"".join(link)
                yield scrapy.http.Request(linkTure, callback =self.func) #回调函数，把linkTure传入Func

        else:
            for sel in response.xpath('//*[@id="wrapper"]/div[1]/div[7]/form[@method]/table/table/tbody/tr/th/span[@id]'):
                #name =sel.xpath('a/text()').extract()
                #item.append(name)
                link = sel.xpath('a/@href').extract()
                linkTure = 'http://38.103.161.187/forum/'+"".join(link)
                yield scrapy.http.Request(linkTure, callback =self.func) #回调函数，把linkTure传入Func


    def func(self,response):

        url = response.xpath('//*/form/div/table/tr/td/div[3]/div[4]/dl/dt/a[2]/@href').extract()
        namepre = response.xpath('//*/form/div/h1/text()').extract()
        name = "".join(namepre)
        urlture = 'http://38.103.161.187/forum/'+"".join(url)
        urllib.urlretrieve(urlture,'%s.torrent'%name)

'''


import scrapy
import urllib
import re
import os

from getSis.items import GetsisItem

num = 0
item = []
class getSisSpider(scrapy.Spider):
    name = "getSis"
    #allowed_domains = ["51job.com"]
    start_urls = [
        #"http://38.103.161.187/forum/forumdisplay.php?fid=25"
        "http://38.103.161.187/forum/forum-25-1.html",
        #"http://38.103.161.187/forum/forum-25-2.html"

    ]
    '''
    page = raw_input("input something?")  #输入你要找的页数
    for page in xrange(2,(int(page)+1)):
        start_urls.append("http://38.103.161.187/forum/forum-25-%d.html"%page)


    '''
    def parse(self, response):
        for sel in response.xpath('//*[@id="wrapper"]/div[1]/div[7]/form[@method]/table/table/table/table/tbody/tr/th/span[@id]'):
            name =sel.xpath('a/text()').extract()
            item.append(name)
            link = sel.xpath('a/@href').extract()
            linkTure = 'http://38.103.161.187/forum/'+"".join(link)
            yield scrapy.http.Request(linkTure, callback =self.func) #回调函数，把linkTure传入Func

    def func(self,response):
        url = response.xpath('//*/form/div/table/tr/td/div[3]/div[4]/dl/dt/a[2]/@href').extract()
        namepre = response.xpath('//*/form/div/h1/text()').extract()
        picture = response.xpath('//*/form/div/table/tr/td/div[3]/div[3]/img[1]/@src').extract()
        name = "".join(namepre)
        name = re.sub(r'/', r'-', name)
        path = os.getcwd()
        os.makedirs(r'%s/%s'%(path,name))
        urlture = 'http://38.103.161.187/forum/'+"".join(url)
        urllib.urlretrieve(picture[0],r'%s/%s/%s.jpg' % (path,name,'1'))


        urllib.urlretrieve(urlture,r'%s/%s/%s.torrent' % (path,name,name) )
        #urllib.urlretrieve(urlture,'%s.torrent' % name )
