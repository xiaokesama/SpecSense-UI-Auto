from ui_tests.pages.base_page import BasePage


class SoftwareVersionPage(BasePage):
    path = '/dashboard/softlist'
    title_keyword = '软件版本'

    name_placeholder = '请输入名称搜索'
    model_placeholder = '输入设备机型查询'
    version_placeholder = '输入版本号查询'

    def search_by_name(self, name):
        self.fill_placeholder(self.name_placeholder, name)
        self.click_button('查询')
        self.wait_spinner_done()

    def search_by_model(self, model):
        self.fill_placeholder(self.model_placeholder, model)
        self.click_button('查询')
        self.wait_spinner_done()

    def search_by_version(self, version):
        self.fill_placeholder(self.version_placeholder, version)
        self.click_button('查询')
        self.wait_spinner_done()