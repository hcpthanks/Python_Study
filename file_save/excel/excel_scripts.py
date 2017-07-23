import xlrd


def xl_read():
    """excel 读取"""
    book = xlrd.open_workbook('product.xls') #读取工作簿
    for sheet in book.sheets():
        print(sheet.name)


def xl_read_data():
    """excel数据读取"""
    book = xlrd.open_workbook('product.xls')
    # sheet = book.sheet_by_index(0) #按照顺序sheet读取
    sheet = book.sheet_by_name('Product') #sheet标签名称Product
    print('工作簿:{}'.format(sheet.name))
    print('数据行数:{}'.format(sheet.nrows))
    print('产品数据')
    print('=' * 50)
    for i in range(sheet.nrows):
        print(sheet.row_values(i)) #获取索引指定的数据行


if __name__ == '__main__':
    xl_read_data()
