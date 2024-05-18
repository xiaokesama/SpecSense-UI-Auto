import os


# 定义函数，用于拼接url
def url_join(*args):
    temp = []
    for arg in args:
        if arg.startswith('/'):
            arg = arg[1:]
        if not arg.endswith('/'):
            arg = arg[:] + '/'
        temp.append(arg)
    return os.path.join(*temp)[:-1]


# 测试函数
if __name__ == '__main__':
    print(url_join('/api', '/v1', '/users'))
