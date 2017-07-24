import time

# def worker(n):
#     print(f'函数执行开始于:{time.ctime()}')
#     time.sleep(n)
#     print(f'函数执行结束于:{time.ctime()}')
#
#
# def main():
#     print(f'[主函数执行开始于:{time.ctime()}]')
#     worker(4)
#     worker(2)
#     print(f'[主函数执行结束于:{time.ctime()}]')



def worker(n):
    print(f'函数执行开始于:{time.ctime()}')
    time.sleep(n)
    print(f'函数执行结束语:{time.ctime()}')

def main():
    print(f'主函数执行开始于:{time.ctime()}')
    worker(4)
    worker(2)
    print(f'主函数执行结束于:{time.ctime()}')

if __name__ == '__main__':
    main()



