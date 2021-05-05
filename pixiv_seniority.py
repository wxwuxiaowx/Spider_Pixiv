import requests
from lxml import etree
from fake_useragent import UserAgent
import re
import download_pixiv


class Pixiv_seniprity():
    urls = []

    # 获取排行榜
    def link_text(self, url):
        headers = {"User-Agent": UserAgent().random}
        r = requests.get(url, headers=headers)
        html_doc = r.text
        elector = etree.HTML(html_doc)
        return elector

    # 排行榜解析
    def link_urlGet(self, elector):
        list_url = []
        # 对排行榜链接进行解析
        ranking_list = elector.xpath(".//div[@class='ranking-image-item']")
        # 提取url、标签、和图片数
        for url in ranking_list:
            ranking_url = url.xpath(".//img/@data-src")[0]
            ranking_tag = url.xpath(".//img/@data-tags")[0]
            count = url.xpath(".//div[@class='page-count']/span/text()")
            ranking_url = ranking_url.replace(str(*re.findall("c/.*?/", ranking_url)), "")
            # print(ranking_url)
            # 处理多p图片
            if len(count) != 0:
                for i in range(1, int(count[0]) + 1):
                    dict = {}
                    url_temp = ranking_url
                    dict['url'] = ranking_url
                    dict['tag'] = ranking_tag
                    list_url.append(dict)
                    ranking_url = url_temp.replace("_p{0}".format(i - 1), "_p{0}".format(i))
            else:
                dict = {}
                dict['url'] = ranking_url
                dict['tag'] = ranking_tag
                list_url.append(dict)
        return list_url

    def __init__(self, url):
        elector = self.link_text(url)
        list_url = self.link_urlGet(elector)
        download_pixiv.download_pixiv().download(list_url)