import json


def json_basic():
    data = {
        'id': 1,
        '课程': 'python',
        '机构': 'HCP',
        '单价': 98.00,
        '网址': 'http://codr.cn'

    }
    print('原始数据')
    print(data)
    json_str = json.dumps(data)
    print(json_str)
    json_data = json.loads(json_str)
    print(json_data)


def json_write_file():
    """写json文档"""
    data = {
        'id': 1,
        '课程': 'python',
        '机构': 'HCP',
        '单价': 98.00,
        '网址': 'http://codr.cn'
    }

    with open('data.json', 'w', encoding='utf8') as f:
        json.dump(data, f)


def json_read_file():
    """读取json文件"""
    with open('data.json', 'r', encoding='utf8') as f:
        data = json.load(f)
        print(data)


def json_type_diff():
    """类型差异"""
    data = {
        'Discountinued': False,
        'Title': 'iphone7s',
        'category': None,
        'price': True
    }
    print(json.dumps(data))

if __name__ == '__main__':
    json_type_diff()