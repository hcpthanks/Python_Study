import csv


def csv_read():
    """读取文件"""
    with open('my_course.csv', 'r', encoding='utf8') as f:
        # reader = csv.reader(f)  #读取到列表
        reader = csv.DictReader(f) #读取到字典表
        headers = next(reader)
        print(headers)
        for row in reader:
            print(row['课程'])


def csv_write():
    """写入csv文件"""
    headers = ['编号', '课程', '讲师']
    rows = [
        (1, 'python', 'hcpthanks'),
        (2, 'python', 'hcpthanks'),
        (3, 'python', 'hcpthanks'),
        (4, 'python', 'hcpthanks')
    ]
    with open('my_course.csv', 'w', encoding='utf8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)


def csv_write_dict():
    """写入csv字典表格式"""
    headers = ['ID', 'Title', 'Org', 'Url']
    rows = [
        {'ID': 1, 'Title': 'Python 入门', 'Org': 'HCP', 'Url': 'http://github.com'},
        {'ID': 2, 'Title': 'Python 入门', 'Org': 'HCP', 'Url': 'http://github.com'},
        {'ID': 3, 'Title': 'Python 入门', 'Org': 'HCP', 'Url': 'http://github.com'},
        {'ID': 4, 'Title': 'Python 入门', 'Org': 'HCP', 'Url': 'http://github.com'},
        dict(ID=5, Title='flask', Org='HCP', Url='http://github.com')
    ]
    with open('my_course1.csv', 'w', encoding='utf8', newline='') as f:
        writer = csv.DictWriter(f, headers)
        writer.writeheader()
        writer.writerows(rows)


if __name__ == '__main__':
    csv_write_dict()
