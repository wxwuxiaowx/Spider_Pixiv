import requests
from fake_useragent import UserAgent
import re
import json
import download_pixiv


class key_pixiv():
    def get_url(self, name, page=1):
        urls = []
        for i in range(0, page):
            url = "https://www.pixiv.net/ajax/search/artworks/" + name + "?word=" + name + "&order=date_d&mode=all&p=" + str(
                page) + "&s_mode=s_tag&type=all&lang=zh"
            urls.append(url)
            print(page)
        print(urls)
        return urls

    def link_text(self, url):
        headers = {"User-Agent": UserAgent().random}
        r = requests.get(url, headers=headers)
        html_doc = r.text
        # elector = etree.HTML(html_doc)
        print(html_doc)
        return html_doc
        # html_doc.replace(r"\\/","/")

    def url_Get(self, html_doc, name):
        url_list = []
        test = json.dumps(html_doc)
        test = test.replace(r"\\/", "/")
        urls = re.findall(r'https://i.pximg.net/c/250x250_80_a2/img-master/img(.*?).jpg', test, re.S)
        # print(len(tags))

        for url in urls:
            dict = {}
            url2 = "https://i.pximg.net/img-master/img" + url + ".jpg"
            url2.replace("square", "master")
            dict['url'] = url2
            dict['tag'] = name
            print(url2)
            url_list.append(dict)
        return url_list

    def __init__(self, name, page):
        urls = self.get_url(name, page)
        for url in urls:
            elector = self.link_text(url)
            list_url = self.url_Get(elector, name)
            download_pixiv.download_pixiv().download(list_url, name=name)
