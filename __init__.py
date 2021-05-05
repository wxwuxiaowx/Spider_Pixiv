import key_pixiv
import pixiv_seniority
import os

def __init__():
    print("-----------目录---------------")
    i = input("请选择："
          "1.日排行榜"
          "2.周排行榜"
          "3.月排行榜"
          "4.关键字爬取"
              "5.退出")
    if not os.path.isdir('pixiv_download/image'):
        os.makedirs('pixiv_download/image')
    if not os.path.isdir('pixiv_download/Cartoon'):
        os.makedirs('pixiv_download/Cartoon')
    if i == '1':
        url2 = "https://www.pixiv.net/ranking.php"
        pixiv_seniority.Pixiv_seniprity(url2)
    elif i == '2':
        url2 = "https://www.pixiv.net/ranking.php?mode=weekly"
        pixiv_seniority.Pixiv_seniprity(url2)
    elif i == '3':
        url2 = "https://www.pixiv.net/ranking.php?mode=monthly"
        pixiv_seniority.Pixiv_seniprity(url2)
    elif i == '4':
        url2 = input("请输入要爬取的关键字：")

        key_pixiv.key_pixiv(url2, 1)
    elif i == '5':
        quit()
while True:
    __init__()
