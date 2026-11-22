from ui_tests.pages.base_page import BasePage


class DeviceLogPage(BasePage):
    path = '/device/LogList'
    title_keyword = '设备日志'

    operator_placeholder = '输入操作人员查询'
    sn_placeholder = '输入设备SN查询'

    def search_by_operator(self, operator):
        self.fill_placeholder(self.operator_placeholder, operator)
        self.click_button('查询')
        self.wait_spinner_done()

    def search_by_sn(self, sn):
        self.fill_placeholder(self.sn_placeholder, sn)
        self.click_button('查询')
        self.wait_spinner_done()