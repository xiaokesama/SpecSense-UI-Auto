import pytest
from playwright.sync_api import expect

from ui_tests.case_objects import MENU_GROUP_CASES


@pytest.mark.parametrize('case', MENU_GROUP_CASES, ids=lambda case: case.case_id)
def test_menu_group_links(device_page, case):
    device_page.open_menu_group(case.menu_name)

    for link_text, href in case.links:
        link = device_page.sidebar_link(href)
        expect(link).to_be_visible()
        expect(link).to_contain_text(link_text)


def test_visitor_and_account_menu_visible(device_page):
    expect(device_page.sidebar_link('/visitor/visitorlist')).to_be_visible()
    expect(device_page.sidebar_link('/isystem/user')).to_be_visible()

    visitor_link = device_page.sidebar_link('/visitor/visitorlist')
    expect(visitor_link).to_contain_text('访客管理')

    account_link = device_page.sidebar_link('/isystem/user')
    expect(account_link).to_contain_text('账号管理')