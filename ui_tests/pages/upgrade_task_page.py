from ui_tests.pages.base_page import BasePage


class UpgradeTaskPage(BasePage):
    path = '/dashboard/upgradetask'
    title_keyword = '升级任务'

    task_placeholder = '请输入任务名称'
    version_placeholder = '请输入版本'

    def search_by_task(self, task_name):
        self.fill_placeholder(self.task_placeholder, task_name)
        self.click_button('查询')
        self.wait_spinner_done()

    def search_by_version(self, version):
        self.fill_placeholder(self.version_placeholder, version)
        self.click_button('查询')
        self.wait_spinner_done()