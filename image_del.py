from PIL import Image
import os


class image_del():
    def __init__(self, filepath):
        files = os.listdir(filepath)
        for file in files:
                    name = filepath+"\\" + file

                    temp = is_color_image(name)
                    print("temp=="+str(temp))
                    if temp:
                        print("del!!!!!")
                        os.remove(name)


def is_color_image(url):
    print(url)
    im = Image.open(url)
    pix = im.convert('RGB')
    width = im.size[0]
    height = im.size[1]
    oimage_color_type = 1
    for x in range(width):
        for y in range(height):
            r, g, b = pix.getpixel((x, y))
            r = int(r)
            g = int(g)
            b = int(b)
            if (r == g) and (g == b):
                pass
            else:
                oimage_color_type = 0
    return oimage_color_type


image_del(r"E:\Python\Spider_pixiv\pixiv_download\image")
