from ui_tests.pages.base_page import BasePage


class VisitorPage(BasePage):
    path = '/visitor/visitorlist'
    title_keyword = '访客管理'

    name_placeholder = '姓名'
    id_card_placeholder = '身份证'

    def search_by_name(self, name):
        self.fill_placeholder(self.name_placeholder, name)
        self.click_button('查询')
        self.wait_spinner_done()

    def search_by_id_card(self, id_card):
        self.fill_placeholder(self.id_card_placeholder, id_card)
        self.click_button('查询')
        self.wait_spinner_done()