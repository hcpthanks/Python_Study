import re
import requests
from urllib.request import urlretrieve



def download_img(url, regex):
    html = requests.get(url).text
    img_srcs = re.findall(regex, html)
    for i, src in enumerate(img_srcs):
        save_name = r'download/{}.png'.format(i + 1)
        urlretrieve(src, save_name)

if __name__ == '__main__':
    download_img()





