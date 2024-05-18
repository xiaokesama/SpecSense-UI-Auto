import yaml
from configparser import ConfigParser


# 封装成类
class Config:
    def __init__(self, config_file,encoding='utf-8'):
        self.config_file = config_file
        self.encoding = encoding
        self.suffix = config_file.split('.')[-1]
        if self.suffix not in ['yaml', 'ini', 'cfg', 'cnf', 'conf', 'yml']:
            raise ValueError('不能识别的文件类型: {}'.format(self.suffix))

    def _parse_yaml(self):
        with open(self.config_file, 'r', encoding=self.encoding) as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
        return data

    def _parse_ini(self):
        config = ConfigParser()
        config.read(self.config_file, encoding=self.encoding)
        data = {}
        for section in config.sections():
            data[section] = dict(config.items(section))
        return data

    def parse(self):
        if self.suffix in ['yaml', 'yml']:
            return self._parse_yaml()
        elif self.suffix in ['ini', 'cfg', 'cnf', 'conf']:
            return self._parse_ini()


if __name__ == '__main__':
    config = Config('../conf.yaml')
    print(config.parse())
    print('-'*20)
    config = Config('../conf.ini')
    print(config.parse())