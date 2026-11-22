from ui_tests.pages.base_page import BasePage


class BlackListPage(BasePage):
    path = '/member/blacklist'
    title_keyword = '黑名单'
    menu_group = '人员管理'

    name_placeholder = '姓名'
    id_card_placeholder = '身份证'
    phone_placeholder = '电话号码'

    def search_by_name(self, name):
        self.fill_placeholder(self.name_placeholder, name)
        self.click_button('查询')
        self.wait_spinner_done()

    def search_by_id_card(self, id_card):
        self.fill_placeholder(self.id_card_placeholder, id_card)
        self.click_button('查询')
        self.wait_spinner_done()

    def search_by_phone(self, phone):
        self.fill_placeholder(self.phone_placeholder, phone)
        self.click_button('查询')
        self.wait_spinner_done()