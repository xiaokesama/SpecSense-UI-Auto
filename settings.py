import os
# 根目录
ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

# 项目域名
PROJECT_HOST = 'http://localhost:8000/'

# 接口地址
INTERFACES = {
    'login': '/api/login',
    'register': '/api/register',
    'recharge': '/menber/recharge',
    'add': '/loan/add',
    'audit': '/loan/audit',
    'invest': '/loan/invest'
}

# 日志配置
LOG_CONFIG = {
    'name':'pylog',
    'filename':'logs/pylog.log',
    'model':'a',
    'debug':True,
    'encoding':'utf-8'
}

# 测试数据配置
TEST_DATA_PATH = os.path.join(ROOT_PATH, 'test_data/test_data.xlsx')

# 测试报告
REPORT_CONFIG = {
    'filename':'测试报告.html',
    'description':'一个练手项目',
    'report_dir':os.path.join(ROOT_PATH,'reports')
}

# 数据库配置
DB_CONFIG = {
    'host': 'localhost',
    'user': 'xiaoke',
    'password': '1193274986xk',
    'db': 'mydb',
    'port': 3306,
    'charset': 'utf8',
}

# 服务器公钥
SERVER_RSA_PUB_KEY = """
-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDQENQujkLfZfc5Tu9Z1LprzedE
O3F7gs+7bzrgPsMl29LX8UoPYvIG8C604CprBQ4FkfnJpnhWu2lvUB0WZyLq6sBr
tuPorOc42+gLnFfyhJAwdZB6SqWfDg7bW+jNe5Ki1DtU7z8uF6Gx+blEMGo8Dg+S
kKlZFc8Br7SHtbL2tQIDAQAB
-----END PUBLIC KEY-----
"""



