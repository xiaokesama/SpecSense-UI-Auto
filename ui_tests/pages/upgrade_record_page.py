from ui_tests.pages.base_page import BasePage


class UpgradeRecordPage(BasePage):
    path = '/dashboard/recordlist'
    title_keyword = '升级记录'

    task_placeholder = '请输入任务名称'
    sn_placeholder = '支持输入多个SN,请用逗号或空格间隔'
    account_placeholder = '请输入账号查询'
    version_placeholder = '请输入版本进行查询'

    def search_by_sn(self, sn):
        self.fill_placeholder(self.sn_placeholder, sn)
        self.click_button('查询')
        self.wait_spinner_done()

    def search_by_account(self, account):
        self.fill_placeholder(self.account_placeholder, account)
        self.click_button('查询')
        self.wait_spinner_done()