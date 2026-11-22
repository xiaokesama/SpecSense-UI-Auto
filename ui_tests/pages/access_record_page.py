from ui_tests.pages.base_page import BasePage


class AccessRecordPage(BasePage):
    path = '/current/accesslist'
    title_keyword = '门禁通行记录'
    menu_group = '通行记录'

    device_placeholder = '输入设备编号查询'
    person_placeholder = '输入人员姓名查询'

    def search_by_device(self, device_no):
        self.fill_placeholder(self.device_placeholder, device_no)
        self.click_button('查询')
        self.wait_spinner_done()

    def search_by_person(self, person_name):
        self.fill_placeholder(self.person_placeholder, person_name)
        self.click_button('查询')
        self.wait_spinner_done()