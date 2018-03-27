# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import re
import scrapy
from leshiRank.items import LeshirankItem
from datetime import datetime

class LerankSpider(scrapy.Spider):
    name = "leRank"
    allowed_domains = ["top.le.com"]
    start_urls = [
        "http://top.le.com/filmhp.html",
        "http://top.le.com/filmhc.html",
        "http://top.le.com/tvhc.html",
        "http://top.le.com/tvhp.html",
        "http://top.le.com/varhp.html",
        "http://top.le.com/comichp.html",
        "http://top.le.com/comichc.html",
        "http://top.le.com/mfilmhp.html",
        "http://top.le.com/mfilmhc.html",
    ]
    subclasses = [u"日", u"周", u"月", u"全部"]

    def parse(self, response):
        html = response.body

        pattern = re.compile(r"<li class=\"selected\">(.*?)</li>")
        search1 = pattern.search(html, re.S)
        classification = search1.group(1).decode("utf-8") if search1 else None

        pattern = re.compile(r"<li class=\"current\">.*?<a.*?>(.*?)</a>")
        channel = pattern.search(html, re.S).group(1).decode("utf-8")

        search2 = response.xpath("//div[@class='chart-data section1']/ol[@class='chart-list j-for']")
        if len(search2) == 1:
            subclass = u"全部"
            for x, li in enumerate(search2[0].xpath("li")):
                if x % 6 == 0:
                    continue
                rank = int(li.xpath("span/i/text()")[0].extract().strip())
                name = li.xpath("span/a/text()")[0].extract().strip()
                nameUrl = li.xpath("span/a/@href")[0].extract().strip()
                infoId = videoId = None
                if channel == u"电影" or channel == u"综艺" or channel == u"网络大电影":
                    videoId = nameUrl.split("/")[-1].split(".")[0]
                else:
                    infoId = nameUrl.split("/")[-1].split(".")[0]
                actors = u"\t".join([actor.strip() for actor in li.xpath("span")[2].xpath("a/text()").extract()]) if len(li.xpath("span")) == 6 else None
                area = li.xpath("span")[-3].xpath("a/text()")[0].extract()
                _type = u"\t".join(li.xpath("span")[-2].xpath("a/text()").extract())
                score = li.xpath("span/text()")[-1].extract().strip()

                item = LeshirankItem()
                item['classification'] = classification
                item['subclass'] = subclass
                item['channel'] = channel
                item['rank'] = rank
                item['name'] = name
                item['nameUrl'] = nameUrl
                item['actors'] = actors
                item['area'] = area
                item['_type'] = _type
                item['score'] = score
                item['listDays'] = None
                item['rankTop'] = None
                item['increment'] = None
                item['trend'] = None
                item['playCount'] = None
                item['infoId'] = infoId
                item['videoId'] = videoId
                item['_date'] = datetime.now().strftime("%Y-%m-%d")
                item['update_time'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                item['create_time'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                yield item
                # print classification, subclass, channel, rank, name, nameUrl, actors, area, _type, score, infoId, videoId
        else:
            for x, _search in enumerate(search2):
                subclass = self.subclasses[x]
                for y, li in enumerate(_search.xpath("li")):
                    if y % 6 == 0:
                        continue

                    numbers = len(li.xpath("span"))

                    rank = int(li.xpath("span/i/text()")[0].extract().strip())
                    name = li.xpath("span/a/text()")[0].extract().strip()
                    nameUrl = li.xpath("span/a/@href")[0].extract().strip()
                    infoId = videoId = None
                    if channel == u"电影" or channel == u"综艺" or channel == u"网络大电影":
                        videoId = nameUrl.split("/")[-1].split(".")[0]
                    else:
                        infoId = nameUrl.split("/")[-1].split(".")[0]
                    trend = li.xpath("span/i/@class")[-1].extract().strip().split("-")[-1] if x != 3 else None
                    playCount = li.xpath("span/text()")[-1].extract().strip().replace(u",", "") if x == 3 else None
                    actors = ("\t".join([actor.strip() for actor in li.xpath("span")[2].xpath("a/text()").extract()])).replace(u'\xc9', "") if numbers == 7 or (numbers == 6 and x == 3) else None
                    area = None
                    if (numbers == 5 and x == 3) or (numbers == 6 and x != 3):
                        area = li.xpath("span")[2].xpath("a/text()")[0].extract().strip()
                    elif numbers <= 5:
                        pass
                    else:
                        area = li.xpath("span")[3].xpath("a/text()")[0].extract().strip()
                    _type = None
                    if (numbers == 6 and x != 3) or (numbers == 5 and x != 3):
                        _type = u"\t".join(li.xpath("span")[3].xpath("a/text()").extract())
                    elif numbers < 5:
                        pass
                    else :
                        _type = u"\t".join(li.xpath("span")[4].xpath("a/text()").extract())

                    item = LeshirankItem()
                    item['classification'] = classification
                    item['subclass'] = subclass
                    item['channel'] = channel
                    item['rank'] = rank
                    item['name'] = name
                    item['nameUrl'] = nameUrl
                    item['actors'] = actors
                    item['area'] = area
                    item['_type'] = _type
                    item['score'] = None
                    item['listDays'] = None
                    item['rankTop'] = None
                    item['increment'] = None
                    item['trend'] = trend
                    item['playCount'] = playCount
                    item['infoId'] = infoId
                    item['videoId'] = videoId
                    item['_date'] = datetime.now().strftime("%Y-%m-%d")
                    item['update_time'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    item['create_time'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                    yield item

                    # print subclass, rank, name, nameUrl, infoId, playCount, trend, actors, area, _type, videoId