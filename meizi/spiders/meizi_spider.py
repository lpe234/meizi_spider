# -*- coding: utf-8 -*-

from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.http.request import Request

import urlparse

from meizi.items import MeiziItem

__author__ = 'lpe234'


class MeiziSpider(Spider):

    name = 'meizi'
    start_urls = ['http://www.meizitu.com/']

    def parse(self, response):
        """
        scrapy 默认入口函数，获取所有分类url（即所有入口）
        :param response:
        :return:
        """
        sel = Selector(response)
        category_nodes = sel.xpath('//div[@class="tags"]/span//a[@title][@href]')
        for node in category_nodes:
            try:
                tag = node.xpath('./@title').extract()[0]
                href = node.xpath('./@href').extract()[0]
                if tag and href:
                    yield Request(
                        url=href,
                        callback=self.parse_list,
                        meta={'data': tag}
                    )
            except(IndexError, TypeError):
                continue

    def parse_list(self, response):
        """
        根据 不同分类 进入列表页，进行遍历（存在分页情况）
        :param response:
        :return:
        """
        tag = response.meta['data']
        sel = Selector(response)

        # 当前页 结点遍历
        nodes = sel.xpath('//ul/li[@class="wp-item"]//h3/a[@href]')
        for node in nodes:
            try:
                title = node.xpath('./b/text()').extract()[0]
                href = node.xpath('./@href').extract()[0]
                if title and href:
                    yield Request(
                        url=href,
                        callback=self.parse_details,
                        meta={'data': '-'.join((tag, title))}
                    )
            except(IndexError, TypeError):
                continue

        # 其他页
        other_pages = sel.xpath('//div[@id="wp_page_numbers"]//li/a[@href]')
        for page in other_pages:
            try:
                href = page.xpath('./@href').extract()[0]
                href = urlparse.urljoin(response.url, href)
                if href:
                    yield Request(
                        url=href,
                        callback=self.parse_list,
                        meta={'data': tag}
                    )
            except(IndexError, TypeError):
                continue

    def parse_details(self, response):
        package_name = response.meta['data']
        images = self.fetch_images(response)

        item = MeiziItem()
        item['name'] = package_name
        item['images'] = images

        yield item

    @classmethod
    def fetch_images(cls, response):
        """
        解析当前页 所有图片
        :param response:
        :return:
        """
        sel = Selector(response)

        images = []
        images_nodes = sel.xpath('//div[@id="picture"]//img[@src]')
        for node in images_nodes:
            try:
                image = node.xpath('./@src').extract()[0]
                if image:
                    images.append(image)
            except(IndexError, TypeError):
                continue
        return images