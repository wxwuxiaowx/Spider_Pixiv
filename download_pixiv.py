import requests
from fake_useragent import UserAgent
import os
class download_pixiv():
    urls = []

    def download(self, list_url, name=None):

        # pprint(list_url)
        for item in list_url:
            if not os.path.isdir('pixiv_download/image'):
                os.makedirs('pixiv_download/image')
            headers = {"User-Agent": UserAgent().Random, 'Referer': item['url']}
            try:
                r = requests.get(item['url'], headers=headers, timeout=5)
                print(r)
                # print(item['url'])
                self.save_pixiv(item, r)
                print("save go")
            except:
                self.urls.append(item)
                print("添加成功")
        time_count = 0
        while len(self.urls) != 0 or time_count < 5:
            print("22222")
            for url in self.urls:
                headers = {"User-Agent": UserAgent().Random, 'Referer': url['url']}
                try:
                    r = requests.get(url['url'], headers=headers, timeout=5)
                    self.save_pixiv(url, r)
                    print(url['url'])
                    self.urls.remove(url)
                except:
                    pass
            time_count += 1

    def save_pixiv(self,item,r):
        print(len(item['tag']))
        if "漫画" in item['tag']:
            name = item['url'].split("/")[-1].split("_")[0].replace(".jpg", "")
            if not os.path.isdir('pixiv_download/Cartoon/{0}'.format(name)):
                os.makedirs('pixiv_download/Cartoon/{0}'.format(name))
            self.create_pixiv_file(
                "pixiv_download/Cartoon/{0}/{1}".format(name, item['url'].split("/")[-1]),
                r.content)
            print("漫画下载成功")
            # time.sleep(0.5)
        # 图片下载
        elif len(item['tag']) < 10:
            if not os.path.isdir('pixiv_download/{0}'.format(item['tag'])):
                os.makedirs('pixiv_download/{0}'.format(item['tag']))
            self.create_pixiv_file('pixiv_download/{0}/{1}'.format(item['tag'],item['url'].split("/")[-1]),r.content)
        else:
            print("picture download")
            self.create_pixiv_file("pixiv_download/image/{0}".format(item['url'].split("/")[-1]), r.content)
            print("图片下载成功")
            # time.sleep(0.5)


    def create_pixiv_file(self, name, byte_r):
        if not os.path.isfile(name):
            with open(name, "wb")as f:
                f.write(byte_r)

