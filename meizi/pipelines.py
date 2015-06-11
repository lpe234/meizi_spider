# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os
import urllib

from meizi.spiders import meizi_spider, imooc_spider

FILE_NAME = 'meizi_images'

class MeiziPipeline(object):
    def process_item(self, item, spider):
        if spider.name == meizi_spider.MeiziSpider.name:
            abs_path = get_abs_path(item)
            save_to_folder(item, abs_path)
        elif spider.name == imooc_spider.ImoocSpider.name:
            pass
        return item


def get_abs_path(item):
    """
    创建文件夹
    :param item:
    :return:
    """
    abs_path = os.path.join(os.getcwd(), FILE_NAME)

    # 确保 ‘meizi_images’ 文件夹已存在
    if not os.path.exists(abs_path):
        os.mkdir(abs_path)

    # 确保 ‘相应文件夹’ 已被创建
    abs_path_ = os.path.join(abs_path, item['name'])
    if not os.path.exists(abs_path_):
        os.mkdir(abs_path_)

    return abs_path_

def save_to_folder(item, abs_path):
    """
    下载并保存图片至相应文件夹
    :param item:
    :param abs_path:
    :return:
    """
    for url in item['images']:
        img_name = url.split('/')[-1]
        img_abs_path = os.path.join(abs_path, img_name)
        urllib.urlretrieve(url, img_abs_path)
