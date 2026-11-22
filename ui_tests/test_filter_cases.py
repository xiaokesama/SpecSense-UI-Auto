import re

import pytest
from playwright.sync_api import expect

from ui_tests.case_objects import FILTER_CASES
from ui_tests.pages import (
    AccessRecordPage,
    AccountPage,
    BlackListPage,
    DeviceLogPage,
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
    'software': SoftwareVersionPage,
    'upgrade_task': UpgradeTaskPage,
    'upgrade_record': UpgradeRecordPage,
    'device_log': DeviceLogPage,
    'person_privilege': PersonPrivilegePage,
    'member_list': MemberListPage,
    'issue_result': IssueResultPage,
    'whitelist': WhiteListPage,
    'blacklist': BlackListPage,
    'access_record': AccessRecordPage,
    'visitor': VisitorPage,
    'account': AccountPage,
}


@pytest.mark.parametrize('case', FILTER_CASES, ids=lambda case: case.case_id)
def test_page_filter_case(device_page, case):
    page_obj = device_page.go_to(PAGE_CLASSES[case.page_key])
    getattr(page_obj, case.method_name)(case.value)

    expect(page_obj.button('重置')).to_be_visible()
    expect(page_obj.page.locator('.ant-table')).to_be_visible()
    expect(page_obj.page).to_have_url(re.compile(re.escape(page_obj.path) + r'$'))

    page_obj.click_button('重置')
    page_obj.wait_spinner_done()
    expect(page_obj.page.locator('.ant-table')).to_be_visible()