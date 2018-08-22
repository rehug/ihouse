# -*- coding: utf-8 -*-

from scrapy.selector import Selector
from scrapy.contrib.spiders import CrawlSpider

from ihouse.items import IhouseItem


class VHouse(CrawlSpider):
    """
    爬取列表页
    """
    name = 'vhouse'
    allowed_domains = ['www.vlinker.com.cn/']
    start_urls = ['http://www.vlinker.com.cn/Community/FindList']

    def parse(self, response):
        item = IhouseItem()
        houses = Selector(response).xpath('//*[@class="map_list"]/ul/li')
        house_href = 'http://www.vlinker.com.cn/CmsApartment/' \
                     'ApartmentDetails?id='
        for house in houses:
            temp_link = house.xpath('div/a/@onclick').extract()
            link = house.xpath('div/a/@onclick').extract()
            for i, j in enumerate(link):
                slice_drop_func = slice(12, -1)
                tlink = j[slice_drop_func].replace('\'', '')
                link[i] = house_href + tlink.split(',')[0]
            title = house.xpath('.//li[2]/text()').extract()
            price = house.xpath('.//li[1]/b/text()').extract()
            address = house.xpath('.//li[3]/i/text()').extract()
            item['title'] = title
            item['price'] = price
            item['address'] = address
            item['link'] = link
            item['origin'] = temp_link
            yield item


