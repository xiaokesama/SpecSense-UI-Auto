import pytest
from playwright.sync_api import expect

from ui_tests.case_objects import PAGE_CASES
from ui_tests.pages import (
    AccessRecordPage,
    AccountPage,
    BlackListPage,
    DepartmentPage,
    DeviceLogPage,
    DevicePage,
    IssueResultPage,
    MemberListPage,
    PersonPrivilegePage,
    SoftwareVersionPage,
    UpgradeRecordPage,
    UpgradeTaskPage,
    VisitorPage,
    WhiteListPage,
)


PAGE_CLASSES = {
    'device': DevicePage,
    'software': SoftwareVersionPage,
    'upgrade_task': UpgradeTaskPage,
    'upgrade_record': UpgradeRecordPage,
    'device_log': DeviceLogPage,
    'department': DepartmentPage,
    'person_privilege': PersonPrivilegePage,
    'member_list': MemberListPage,
    'issue_result': IssueResultPage,
    'whitelist': WhiteListPage,
    'blacklist': BlackListPage,
    'access_record': AccessRecordPage,
    'visitor': VisitorPage,
    'account': AccountPage,
}


@pytest.mark.parametrize('case', PAGE_CASES, ids=lambda case: case.case_id)
def test_page_buttons_and_headers(device_page, case):
    page_obj = device_page.go_to(PAGE_CLASSES[case.page_key])

    for button_text in case.buttons:
        expect(page_obj.button(button_text)).to_be_visible()

    if case.table_expected:
        expect(page_obj.page.locator('.ant-table')).to_be_visible()
        page_obj.expect_headers(case.headers)


def test_switch_pages_and_back(device_page):
    software_page = device_page.go_to(SoftwareVersionPage)
    expect(software_page.sidebar_link('/dashboard/softlist')).to_be_visible()

    account_page = software_page.go_to(AccountPage)
    expect(account_page.sidebar_link('/isystem/user')).to_be_visible()

    back_to_device = account_page.go_to(DevicePage)
    expect(back_to_device.page).to_have_url('http://172.168.80.54/dashboard/analysis')
    expect(back_to_device.rows().first).to_be_visible()