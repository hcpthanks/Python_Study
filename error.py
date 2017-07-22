# try:
#     x = 5 / 0
# except ZeroDivisionError as e:
#     print('不能除令', e)
# except:
#     print('其他错误')
#
# else:
#     print('没有异常')

# for i in range(10):
#     print(f'i = {i}')
#     print(i ** 2)
#

a = 1.1
b = 2.2

if round(a + b, 1) == 3.3:
    x = 5
    y = 3
    z = x / y
    print(z)


# class Person:
#     def __init__(self, name):
#         self.name = name
#
# p = Person('peter')

# try:
#     print(p.age)
# except AttributeError as e:
#     print('属性异常')

# f = open('data.txt')
# try:
#     f.read()
# except:
#     print('文件操作遇到错误')
#
# finally:
#     f.close()