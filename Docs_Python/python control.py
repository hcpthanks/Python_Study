# x = int(input('please enter an integer:'))
#
#
# if x < 0:
#     x = 0
#     print('negative changed to zero')
# elif x == 0:
#     print('zero')
#
# elif x == 1:
#     print('single')
# else:
#     print('more')
#
#

# words = ['cat', 'window', 'defenestrate']
# for w in words:
#     print(w, len(w))
#
# ======================
# cat 3
# window 6
# defenestrate 12

# for w in words[:]:
#     if len(w) > 6:
#         words.insert(0, w)
#
# print(words)

# r = range(5, 10)
# r = range(0, 10, 3)
# r = range(-10, -100, -30)  #-10, -40, -70
#
# print(list(r))

#搜索质数
# for n in range(2, 10):
#     for x in range(2,n):
#         if n % x ==0:
#             print(n, 'equals', x, '*', n//x)
#             break
#     else:
#         print(n, 'is a prime number')
#

# #continue
# for num in range(2, 10):
#     if num % 2 == 0:
#         print('found an even number', num)
#         continue
#     print('found a number', num)

# pass语句用于语法上必须要有什么语句,但程序上什么也不做的场合
# while True:
#     pass
#
#
#
# class MyEmptyClass:  #构建最小结构的类
#     pass

#
# def initlog(*args):
#     pass            # 做函数或控制体的占位符


#定义函数
#构建一个用来生成指定边界的斐波那契数列函数:
# def fib(n):
#     """print a fibonacci series up to n."""
#     a, b = 0, 1
#     while a < n:
#         print(a, end=',')
#         a, b = b, a+b
#     print()
#
# fib(2000)  #调用函数

# def fib2(n):  # return fibonacci series up to n
#     """Return a fibonacci series up to n."""
#     result = []
#     a, b = 0, 1
#     while a < n:
#         result.append(a)  #see below
#         a, b = b, a+b
#     return result
#
# print(fib2(100))  #call it


# i = 5
# def f(arg=i):
#     print(arg)
#
# i = 6
# f()

#计算出现次数
# a = [66.25, 333, 333, 1, 1234.5]
# print(a.count(333), a.count(66.25), a.count('x'))


#把列表当做队列使用
#队列作为特定的数据结构, 最先进入的元素最先释放(先进先出)
#不过,这样使用效率不高. 相对来说从列表末尾添加和弹出很快;
#在头部插入和弹出很慢(因为,为了一个元素,要移动整个列表中所有的元素)

# from collections import deque
# queue = deque(['eric', 'john', 'michael'])
# queue.append('terry')   # terry arrives
# queue.append('graham')  # graham arrives
# queue.popleft()         # eric-- the first to arrive now leaves
# queue.popleft()         # john --the second to arrive now leaves
# print(queue)            # deque(['michael', 'terry', 'graham'])


#列表推导
# squares = []
# for x in range(10):
#     squares.append(x ** 2)


# squares = list(map(lambda x: x ** 2, range(10)))

# squares = [x ** 2 for x in range(15)]
#
# print(squares)

# r = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
# print(r)

# 答案 [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

#等同于:

# combs = []
# for x in [1, 2, 3]:
#     for y in[3, 1, 4]:
#         if x != y:
#             combs.append((x, y))
# print(combs[1])

#列表推导 可使用复杂的表达式和嵌套函数
# from math import pi
# [str(round(pi, i))for i in range(1, 6)]
# ['3.1', '3.14', '3.142', '3.1416', '3.14159']

vec = [-4, -2, 0, 2, 4]
# creat a new list with the values doubled
[x * 2 for x in vec]     #[-8, -4, 0, 4, 8]

# filter the list to exclude negative numbers
[x for x in vec if x >= 0]   # [0, 2, 4]

#apply a function to all the elements
[abs(x) for x in vec]    #[4, 2, 0, 2, 4]

#call a method on each element
freshfruit = ['  banana', 'loganberry', 'passion fruit  ']
[weapon.strip()for weapon in freshfruit]

#create a list of 2-tuples like (number, square)
[(x, x ** 2) for x in range(6)]
#[(0, 0), (1, 1), (2, 4), (3, 9),(4, 16), (5, 25)]

flatten a list using a listcomp with two 'for'
vec = [[1,2,3], [4, 5, 6], [7, 8, 9]]
[num for elem in vec for num in elem]    #[1, 2, 3, 4, 5, 6, 7, 8, 9]



matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

#现在你想交换列和行, 用嵌套列表推导
[[row[i] for row in matrix] for i in range(4)]
#[[1, 5, 9], [2, 6, 10],[3, 7, 11],[4, 8, 12]]

#等同于:
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])

#等同于;
transposed = []
for i in range(4):
    #the following 3 lines implement the nested listcomp
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

#等同于
list(zip(*matrix))
#[[1, 5, 9], [2, 6, 10],[3, 7, 11],[4, 8, 12]]




