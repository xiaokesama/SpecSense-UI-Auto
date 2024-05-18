import unittest

from common.myddt import data,ddt
from common.data_handler import get_test_data_from_excel
from testcases.base_case import BaseCase
import settings

# 从excel中获取测试用例
cases = get_test_data_from_excel(settings.TEST_DATA_PATH,'register')


@ddt
class TestRegister(BaseCase):
    name = '注册'

    @data(*cases)
    def test_register(self, case):
        self.check_case(case)


if __name__ == '__main__':
    unittest.main()
