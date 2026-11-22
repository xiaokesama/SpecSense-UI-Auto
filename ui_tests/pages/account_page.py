from playwright.sync_api import expect

from ui_tests.pages.base_page import BasePage


class AccountPage(BasePage):
    path = '/isystem/user'
    title_keyword = '账号管理'

    account_placeholder = '输入账号模糊查询'
    name_placeholder = '请输入用户名称'

    def search_by_account(self, account):
        self.fill_placeholder(self.account_placeholder, account)
        self.click_button('查询')
        self.wait_spinner_done()

    def search_by_name(self, name):
        self.fill_placeholder(self.name_placeholder, name)
        self.click_button('查询')
        self.wait_spinner_done()

    def open_add_user_drawer(self):
        self.click_button('添加用户')
        drawer = self.drawer()
        expect(drawer).to_be_visible()
        expect(drawer.locator('.ant-drawer-title')).to_have_text('新增')
        return drawer