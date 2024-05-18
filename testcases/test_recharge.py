import json
import unittest

from common.make_request import send_http_request
from common.myddt import data,ddt
from common.data_handler import get_test_data_from_excel,generate_phone,replace_args_by_re
from common.utils import url_join
from common import logger,db
from common.fixture import register,login
from testcases.base_case import BaseCase
import settings

# 从excel中获取测试用例
cases = get_test_data_from_excel(settings.TEST_DATA_PATH,'recharge')


@ddt
class TestRecharge(BaseCase):
    name='充值接口'

    @classmethod
    def setUpClass(cls) -> None:
        cls.logger.info('{}开始测试'.format(cls.name))
        # 1. 注册
        mobilephone = generate_phone()
        pwd = '123456'
        if not register(mobilephone,pwd):
            cls.logger.error('用户注册{}失败'.format(mobilephone))
            raise ValueError('用户注册{}失败'.format(mobilephone))
        cls.logger.info('用户注册{}成功'.format(mobilephone))
        # 2. 登录
        data = login(mobilephone,pwd)
        if data is None:
            cls.logger.error('用户登录{}失败'.format(mobilephone))
            raise ValueError('用户登录{}失败'.format(mobilephone))
        cls.logger.info('用户登录{}成功'.format(mobilephone))
        cls.member_id = data['id']
        cls.token = data['token_info']['token']
        cls.logger.info('获取用户{}的token成功'.format(mobilephone))

    @data(*cases)
    def test_recharge(self,case):
        self.check_case(case)


if __name__ == '__main__':
    unittest.main()
