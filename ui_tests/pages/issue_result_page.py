from ui_tests.pages.base_page import BasePage


class IssueResultPage(BasePage):
    path = '/member/issurelist'
    title_keyword = '人员下发结果'
    menu_group = '人员管理'

    name_placeholder = '人员名称'
    sn_placeholder = 'SN码'

    def search_by_name(self, name):
        self.fill_placeholder(self.name_placeholder, name)
        self.click_button('查询')
        self.wait_spinner_done()

    def search_by_sn(self, sn):
        self.fill_placeholder(self.sn_placeholder, sn)
        self.click_button('查询')
        self.wait_spinner_done()