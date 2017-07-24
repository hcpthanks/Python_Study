import requests
import re


def extra_link():
    url = 'http://www.xinshipu.com/caipu/17844'
    base_url = 'http://xinshipu.com'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        html = r.text
        links = re.findall(r'<a href="(.*?)" title=".*" class="shipu">', html)
        with open('data4.txt', 'w', encoding='utf8') as f:
            for link in links:
                f.write(f'{base_url}{link}\n')


if __name__ == '__main__':
    extra_link()
