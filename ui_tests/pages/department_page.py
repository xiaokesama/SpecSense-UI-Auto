from playwright.sync_api import expect

from ui_tests.pages.base_page import BasePage


class DepartmentPage(BasePage):
    path = '/isystem/depart'
    title_keyword = '部门管理'
    menu_group = '人员管理'
    has_table = False

    def wait_loaded(self):
        super().wait_loaded()
        expect(self.button('树操作')).to_be_visible()
        expect(self.page.get_by_text('当前选择：', exact=False)).to_be_visible()

    def add_group(self):
        self.click_button('添加分组')

    def add_child_group(self):
        self.click_button('添加下级')