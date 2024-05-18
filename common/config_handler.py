import yaml
from configparser import ConfigParser


# 封装成方法
# 返回字典
def get_config(filename,encoding='utf-8') -> dict:
    '''
    获取配置文件内容
    :param filename: 文件名
    :param encoding: 文件编码
    :return: data
    '''
    # 获取后缀名
    suffix = filename.split('.')[-1]
    if suffix in ['yaml', 'yml']:
        with open(filename,'r',encoding=encoding) as f:
            data=yaml.load(f,Loader=yaml.FullLoader)
    elif suffix in ['ini', 'cfg', 'conf']:
        config = ConfigParser()
        config.read(filename, encoding=encoding)
        data = {}
        for section in config.sections():
            data[section] = dict(config.items(section))
    else:
        raise ValueError('Unsupported file type')
    return data


if __name__ == '__main__':
    data = get_config('../conf.ini')
    print(data)
    print('-'*20)
    data = get_config('../conf.yaml')
    print(data)
