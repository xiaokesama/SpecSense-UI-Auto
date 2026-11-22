import re

import pytest
from playwright.sync_api import expect

from ui_tests.case_objects import DEVICE_COLUMN_CASE, DEVICE_DRAWER_CASE, DEVICE_SEARCH_CASES


def test_dashboard_loads(device_page):
    expect(device_page.page).to_have_title(re.compile('多光谱物理感知云平台'))
    expect(device_page.page.get_by_text('欢迎您，系统管理员1', exact=False)).to_be_visible()
    expect(device_page.sidebar_link('/dashboard/analysis')).to_be_visible()
    assert device_page.rows().count() > 0
    expect(device_page.page.locator('.ant-pagination')).to_contain_text(
        re.compile(r'第 \d+-\d+ 条，共 \d+ 条')
    )


def test_search_device_by_current_sn(device_page):
    old_count = device_page.rows().count()
    sn = device_page.first_sn()
    assert sn

    device_page.search_by_sn(sn)
    expect(device_page.rows()).to_have_count(1)
    expect(device_page.rows().first).to_contain_text(sn)
    expect(device_page.page.locator('.ant-pagination')).to_contain_text('共 1 条')

    device_page.reset()
    expect(device_page.rows()).to_have_count(old_count)


@pytest.mark.parametrize('case', DEVICE_SEARCH_CASES, ids=lambda case: case.case_id)
def test_device_search_cases(device_page, case):
    device_page.search_by_sn(case.keyword)

    if case.empty_expected:
        expect(device_page.empty_text()).to_be_visible()
        expect(device_page.rows()).to_have_count(0)
    else:
        expect(device_page.rows().first).to_contain_text(case.keyword)
        assert device_page.rows().count() >= 1

    device_page.reset()
    expect(device_page.rows().first).to_be_visible()


def test_column_filter_dropdown(device_page):
    dropdown = device_page.open_column_filter()
    for column in DEVICE_COLUMN_CASE.columns:
        expect(dropdown).to_contain_text(column)

    device_page.page.keyboard.press('Escape')
    expect(dropdown).to_be_hidden()


def test_add_device_drawer_open_and_cancel(device_page):
    drawer = device_page.open_add_drawer()
    expect(drawer.locator('.ant-drawer-title')).to_have_text(DEVICE_DRAWER_CASE.drawer_title)

    for field in DEVICE_DRAWER_CASE.fields:
        expect(drawer.get_by_placeholder(field)).to_be_visible()

    # 只测取消，不提交，避免往测试环境写脏数据
    device_page.cancel_drawer()


def test_search_by_name_then_reset(device_page):
    old_count = device_page.rows().count()
    device_page.search_by_name('2102233')
    expect(device_page.rows().first).to_contain_text('2102233')

    device_page.reset()
    expect(device_page.rows()).to_have_count(old_count)