import re

from playwright.sync_api import expect


class BasePage:
    path = ''
    title_keyword = ''
    menu_group = ''
    table_body_index = 0
    has_table = True

    def __init__(self, page):
        self.page = page

    def wait_loaded(self):
        expect(self.page).to_have_url(re.compile(re.escape(self.path) + r'$'))
        expect(self.page).to_have_title(re.compile(self.title_keyword))
        if self.has_table:
            self.wait_table()

    def button(self, text):
        return self.page.locator('button').filter(has_text=text).first

    def click_button(self, text):
        self.button(text).click(timeout=8000)

    def fill_placeholder(self, placeholder, value):
        self.page.get_by_placeholder(placeholder).fill(value)

    def wait_table(self):
        self.page.locator('.ant-table').first.wait_for(state='visible')

    def wait_spinner_done(self):
        self.page.wait_for_function(
            """() => !document.querySelector('.ant-spin-spinning')""",
            timeout=15000,
        )

    def wait_first_row(self, index=None):
        body_index = self.table_body_index if index is None else index
        self.page.wait_for_function(
            """(index) => {
                const body = document.querySelectorAll('.ant-table-tbody')[index]
                return body && body.querySelectorAll('tr').length > 0
            }""",
            arg=body_index,
            timeout=15000,
        )

    def rows(self, index=None):
        body_index = self.table_body_index if index is None else index
        return self.page.locator('.ant-table-tbody').nth(body_index).locator('tr')

    def table_headers(self):
        headers = self.page.locator('.ant-table-thead th').all_inner_texts()
        return [x.strip() for x in headers if x.strip()]

    def sidebar_link(self, path):
        return self.page.locator('a[href="{}"]'.format(path))

    def open_menu_group(self, group):
        title = self.page.locator('.ant-menu-submenu-title').filter(has_text=group).first
        if not title.count():
            return

        parent_class = title.locator('xpath=..').get_attribute('class') or ''
        if 'ant-menu-submenu-open' not in parent_class:
            title.click(timeout=8000)
            self.page.wait_for_timeout(250)

    def go_to(self, page_class):
        link = self.sidebar_link(page_class.path)
        if not link.is_visible() and page_class.menu_group:
            self.open_menu_group(page_class.menu_group)

        self.sidebar_link(page_class.path).click(timeout=8000)
        target = page_class(self.page)
        target.wait_loaded()
        return target

    def drawer(self):
        return self.page.locator('.ant-drawer-open').last

    def cancel_drawer(self):
        drawer = self.drawer()
        drawer.locator('.drawer-bootom-button button').first.click(timeout=8000)

        # 个别抽屉的“取消”按钮没有绑定关闭事件，兜底点右上角关闭
        try:
            expect(self.page.locator('.ant-drawer-open')).to_have_count(0, timeout=1500)
        except AssertionError:
            drawer.locator('.ant-drawer-close').click(timeout=8000)
            expect(self.page.locator('.ant-drawer-open')).to_have_count(0)

    def expect_headers(self, expected_headers):
        actual = self.table_headers()
        for header in expected_headers:
            assert header in actual, '表头里没有找到：{}'.format(header)