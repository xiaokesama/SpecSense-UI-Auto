import pytest
from playwright.sync_api import expect

from ui_tests.case_objects import DRAWER_CASES
from ui_tests.pages import AccountPage, DevicePage, MemberListPage


DRAWER_PAGES = {
    'device': DevicePage,
    'account': AccountPage,
    'member_list': MemberListPage,
}

DRAWER_METHODS = {
    'device': 'open_add_drawer',
    'account': 'open_add_user_drawer',
    'member_list': 'open_add_member_drawer',
}


@pytest.mark.parametrize('case', DRAWER_CASES, ids=lambda case: case.case_id)
def test_add_drawer_case(device_page, case):
    if case.page_key == 'device':
        page_obj = device_page
    else:
        page_obj = device_page.go_to(DRAWER_PAGES[case.page_key])

    drawer = getattr(page_obj, DRAWER_METHODS[case.page_key])()
    expect(drawer.locator('.ant-drawer-title')).to_have_text(case.drawer_title)

    for field in case.fields:
        expect(drawer.get_by_placeholder(field)).to_be_visible()

    page_obj.cancel_drawer()