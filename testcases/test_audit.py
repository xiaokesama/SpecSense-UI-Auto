import json
import unittest

import settings
from common import logger, db
from common.fixture import register, login, add_loan
from common.make_request import send_http_request
from common.utils import url_join
from testcases.base_case import BaseCase
from common.data_handler import generate_phone,get_test_data_from_excel,replace_args_by_re
from common.myddt import ddt, data

cases = get_test_data_from_excel(settings.TEST_DATA_PATH, 'audit')


@ddt
class TestAudit(BaseCase):
    logger = logger
    db = db

    @classmethod
    def setUpClass(cls) -> None:
        cls.logger.info('审核接口开始测试')
        # 类前置
        # 1.注册一个普通用户
        mobile_phone = generate_phone()
        pwd = '123456'
        if not register(mobilephone=mobile_phone, pwd=pwd):
            cls.logger.error('注册用户{}失败'.format(mobile_phone))
            raise ValueError('注册用户{}失败'.format(mobile_phone))
        cls.logger.info('注册用户{}成功'.format(mobile_phone))
        # 2.登录这个用户
        data = login(mobilephone=mobile_phone, pwd=pwd)
        if data is None:
            cls.logger.error('登录用户{}失败'.format(mobile_phone))
            raise ValueError('登录用户{}失败'.format(mobile_phone))
        cls.logger.info('登录用户{}成功'.format(mobile_phone))
        # 3. 保存需要的数据能够在这个类的生命周期类共享
        # 将数据保存在类属性中
        # 普通用户的member_id和token
        cls.normal_member_id = data['id']
        cls.normal_token = data['token_info']['token']
        # 4. 注册一个管理员用户
        mobile_phone = generate_phone()
        if not register(mobilephone=mobile_phone, pwd=pwd, _type=0):
            cls.logger.error('注册管理员用户{}失败'.format(mobile_phone))
            raise ValueError('注册管理员用户{}失败'.format(mobile_phone))
        cls.logger.info('注册管理员用户{}成功'.format(mobile_phone))
        # # 5. 登录管理员用户
        data = login(mobilephone=mobile_phone, pwd=pwd)
        if data is None:
            cls.logger.error('登录管理员用户{}失败'.format(mobile_phone))
            raise ValueError('登录管理员用户{}失败'.format(mobile_phone))
        # 6. 保存数据
        # 管理员用户的token
        cls.token = data['token_info']['token']

    def setUp(self) -> None:
        '''
        方法级前置，每个用例前创建一个项目
        :return:
        '''
        res = add_loan(member_id=self.normal_member_id, token=self.normal_token)
        if res:
            self.logger.info('添加项目成功')
            # 保存项目id到类属性中，传递给当前的测试方法
            # 属性名loan_id与用例数据中的槽位名一致
            self.__class__.loan_id = res['id']
        else:
            self.logger.error('添加项目失败！')
            raise ValueError('添加项目失败')

    @data(*cases)
    def test_audit(self, case):
        self.check_case(case)