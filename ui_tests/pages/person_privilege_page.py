from ui_tests.pages.base_page import BasePage


class PersonPrivilegePage(BasePage):
    path = '/member/privilagelist'
    title_keyword = '人员权限'
    menu_group = '人员管理'

    device_placeholder = '设备名称'
    sn_placeholder = 'SN码'

    def search_by_device(self, device_name):
        self.fill_placeholder(self.device_placeholder, device_name)
        self.click_button('查询')
        self.wait_spinner_done()

    def search_by_sn(self, sn):
        self.fill_placeholder(self.sn_placeholder, sn)
        self.click_button('查询')
        self.wait_spinner_done()