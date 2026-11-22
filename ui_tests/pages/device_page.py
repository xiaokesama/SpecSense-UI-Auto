from playwright.sync_api import expect

from ui_tests.pages.base_page import BasePage


class DevicePage(BasePage):
    path = '/dashboard/analysis'
    title_keyword = '多光谱物理感知云平台'
    table_body_index = 1

    name_placeholder = '输入设备名称查询'
    sn_placeholder = '支持输入多个SN,请用逗号或空格间隔'

    def wait_loaded(self):
        super().wait_loaded()
        self.wait_spinner_done()
        self.wait_first_row()

    def first_sn(self):
        return self.rows().first.locator('td').nth(2).inner_text().strip()

    def search_by_sn(self, sn):
        self.fill_placeholder(self.sn_placeholder, sn)
        self.click_button('查询')
        self.wait_spinner_done()

    def search_by_name(self, name):
        self.fill_placeholder(self.name_placeholder, name)
        self.click_button('查询')
        self.wait_spinner_done()

    def reset(self):
        self.click_button('重置')
        self.wait_spinner_done()

    def open_add_drawer(self):
        self.click_button('添加设备')
        drawer = self.drawer()
        expect(drawer).to_be_visible()
        expect(drawer.locator('.ant-drawer-title')).to_have_text('新增')
        return drawer

    def open_column_filter(self):
        self.click_button('筛选列')
        dropdown = self.page.locator('.ant-dropdown:visible').last
        expect(dropdown).to_be_visible()
        return dropdown

    def empty_text(self):
        return self.page.get_by_text('暂无数据', exact=True)