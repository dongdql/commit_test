# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class IIEItem(scrapy.Item):
    # 关键词
    keywords = scrapy.Field()
    # 关键词 id
    subject_id = scrapy.Field()
    # 发现时间
    input_time = scrapy.Field()
    # 直播平台名称
    platform = scrapy.Field()
    # 直播间名称
    roomName = scrapy.Field()
    # 直播间缩略图
    roomImageUrl = scrapy.Field()
    # 直播间地址
    roomUrl = scrapy.Field() #
    # 人气数目
    fans = scrapy.Field() 
    # 直播间主播名字
    zbName = scrapy.Field()
    # 直播 频道
    channel = scrapy.Field()
    