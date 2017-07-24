import requests
from bs4 import BeautifulSoup
import time

course_list_url = 'https://ke.qq.com/course/list'


def extra_links(pages=1):
    with open('course_links.txt', 'w', encoding='utf8') as f:
        for page in range(1, pages + 1):
            page_url = f'{course_list_url}?page={page}'
            r = requests.get(page_url)
            if r.status_code == 200:
                html = r.text
                soup = BeautifulSoup(html, 'html.parser')
                course_list = soup.find(class_='main-left')
                links = course_list.find_all(class_='item-img-link')
                for link in links:
                    href = link.attrs['href']
                    f.write(f'https:{href}\n')

if __name__ == '__main__':
    print(f'主程序开始于:{time.ctime()}')

    extra_links(10)

    print(f'主程序结束于:{time.ctime()}')
