from testcases.base_case import BaseCase
from common.myddt import ddt, data
from common.data_handler import get_test_data_from_excel

cases = get_test_data_from_excel(BaseCase.settings.TEST_DATA_PATH, 'invest_flow')


@ddt
class TestInvestFlow(BaseCase):
    name = '投资业务流'

    @data(*cases)
    def test_invest_flow(self, case):
        self.check_case(case)