# 单独封装:测试数据处理、测试步骤、响应状态码断言、响应数据断言、数据库断言
import json
from jsonpath import jsonpath
import unittest
import requests

from common.make_request import send_http_request
from common.myddt import data,ddt
from common.data_handler import get_test_data_from_excel,generate_phone,replace_args_by_re
from common.utils import url_join
from common import logger,db
import settings


class BaseCase(unittest.TestCase):
    name="base用例"
    logger=logger
    settings=settings
    db=db
    session=requests.Session()

    @classmethod
    def setUpClass(cls):
        # 读取测试数据
        cls.logger.info('{}接口开始测试'.format(cls.name))

    @classmethod
    def tearDownClass(cls):
        cls.logger.info('{}接口测试结束'.format(cls.name))

    def send_http_request(self, url, method, **kwargs) -> requests.Response:
        method = method.lower()
        return getattr(self.session, method)(url, **kwargs)

    def check_case(self,case):
        self.case=case
        self.logger.info('用例：{}开始测试'.format(self.case['title']))
        # 1.测试数据处理
        self.pre_test_data()
        # 2.测试步骤
        self.step()
        # 3.响应状态码断言
        self.assert_status_code()
        # 4.响应数据断言
        self.assert_json_response()
        # 5.数据库断言
        self.assert_db_true()
        # 6.提取数据,作为下一个用例的参数
        self.extract_data()
        self.logger.info('用例[{}]测试结束<<<<<<<<'.format(case['title']))

    def pre_test_data(self):
        # 替换数据
        self.case['request'] = replace_args_by_re(self.case['request'], self)
        # 替换sql
        if self.case['sql']:
            self.case['sql'] = replace_args_by_re(self.case['sql'], self)
        # 生成手机号
        if '#phone#' in self.case['request']:
            phone = generate_phone()
            self.case['request'] = self.case['request'].replace('#phone#', phone)
            if self.case.get('sql'):
                self.case['sql'] = self.case['sql'].replace('#phone#', phone)
        # 拼接地址,可以在xlsx里面写完整的绝对路径，这里就不用拼接了
        if not self.case['url'].startswith('http'):
            self.case['url'] = url_join(settings.PROJECT_HOST, settings.INTERFACES[self.case['url']])
        # json字符串转python对象
        try:
            self.case['request'] = json.loads(self.case['request'])
            self.case['expect_data'] = json.loads(self.case['expect_data'])
        except Exception as e:
            self.logger.exception('用例【{}】json格式错误：'.format(self.case['title']))
            self.logger.debug("case['request']:{}".format(self.case['request']))
            self.logger.debug('case["expect_data"]:{}'.format(self.case['expect_data']))
            raise ValueError('用例[{}]json格式有误'.format(self.case['title']))

    def step(self):
        try:
            # 调用send_http_requests方法发送请求
            self.response = self.send_http_request(url=self.case['url'], method=self.case['method'], **self.case['request'])
        except Exception as e:
            self.logger.exception('用例[{}]发送http请求错误'.format(self.case['title']))
            self.logger.debug(
                'url:{},method:{},request:{}'.format(self.case['url'], self.case['method'], self.case['request']))
            raise e

    def assert_status_code(self):
        try:
            self.assertEqual(self.case['status_code'], self.response.status_code)
        except AssertionError as e:
            self.logger.exception('用例【{}】状态码断言失败：'.format(self.case['title']))
            raise e
        else:
            self.logger.info('用例【{}】状态码断言成功：'.format(self.case['title']))

    def assert_json_response(self):
        # 3.2响应结果断言
        re_data = self.response.json()
        res = {'code': re_data['code'], 'msg': re_data['msg']}
        try:
            self.assertEqual(self.case['expect_data'], res)
        # 当断言失败时，抛出异常，输出日志
        except AssertionError as e:
            self.logger.exception('请求结果断言失败')
            self.logger.debug('期望数据：{}'.format(self.case['expect_data']))
            self.logger.debug('实际数据：{}'.format(res))
            self.logger.debug('响应数据：{}'.format(re_data))
            raise e
        # 定义无异常时打印日志内容
        else:
            self.logger.info('请求结果断言成功')

    def assert_db_true(self):
        if self.case['sql']:
            # 查询数据
            try:
                db_res = self.db.exist(self.case['sql'])
                self.assertTrue(db_res)
            except Exception as e:
                self.logger.exception('用例[{}]数据库断言失败'.format(self.case['title']))
                self.logger.debug('执行的sql是：{}'.format(self.case['sql']))
                raise e
            else:
                self.logger.info('数据库断言成功')

    # 响应数据里面提取作为参数输入下一个用例
    def extract_data(self):
        if self.case.get('extract'):
            try:
                exps = json.loads(self.case['extract'])
            except Exception as e:
                self.logger.exception('用例[{}]提取数据格式错误'.format(self.case['title']))
                self.logger.debug('case["extract"]:{}'.format(self.case["extract"]))
                raise ValueError('用例[{}]的extract提取表达式格式不正确'.format(self.case['title']))

            for _ in exps:
                name = _['name']
                exp = _['exp']
                res = jsonpath(self.response.json(), exp)

                if res:
                    setattr(self.__class__, name, res[0])
                else:
                    raise ValueError('用例[{}]的extract提取表达式[{}]没有匹配到数据'.format(self.case['title'], exp))







