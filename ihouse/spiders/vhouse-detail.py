# -*- coding: utf-8 -*-

import pandas as pd
from scrapy.selector import Selector
from scrapy.contrib.spiders import CrawlSpider

from ihouse.items import IhouseDetail


class VHouseDetail(CrawlSpider):
    """
    爬取详情页
    """
    name = 'vhouse-detail'
    allowed_domains = ['www.vlinker.com.cn/']
    data = pd.read_csv('test.csv')
    urls = data[data['link'] >= ""]['link'].values
    start_urls = [url for url in urls]

    def parse(self, response):
        item = IhouseDetail()

        basic_info = Selector(response).xpath('body/div[4]/div/ul/li')
        title = basic_info[0].xpath('h1/text()').extract()
        address = basic_info[1].xpath('h2/text()').extract()
        phone = basic_info[2].xpath('h2/text()').extract()
        traffic = basic_info[3].xpath('h2/text()').extract()

        show_info = Selector(response).\
            xpath('//*[@class="work_show"]/em/span/text()').extract()
        location = Selector(response).\
            xpath('//*[@class="location"]//ul//span/text()').extract()

        link = response.url

        item['title'] = title
        item['address'] = address
        item['phone'] = phone
        item['traffic'] = traffic
        item['show'] = show_info
        item['location'] = location
        item['link'] = link

        yield item


