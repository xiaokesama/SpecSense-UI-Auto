import os
from pathlib import Path

import pytest
from playwright.sync_api import sync_playwright

from ui_tests.pages.device_page import DevicePage


DEFAULT_DASHBOARD_URL = 'http://172.168.80.54/dashboard/analysis'
DEFAULT_CHROME_PROFILE = Path.home() / 'AppData/Local/Google/Chrome/User Data'


def get_cdp_ws():
    # 优先用环境变量，换机器或者用独立 Chrome 的时候不用改代码
    ws = os.getenv('UI_CDP_WS')
    if ws:
        return ws

    profile = Path(os.getenv('UI_CHROME_PROFILE', DEFAULT_CHROME_PROFILE))
    active_port = profile / 'DevToolsActivePort'
    if not active_port.exists():
        pytest.fail(
            '没找到 Chrome 的 DevToolsActivePort，请先打开 chrome://inspect/#remote-debugging 并允许远程调试'
        )

    port, ws_path = active_port.read_text(encoding='utf-8').splitlines()[:2]
    return 'ws://127.0.0.1:{}{}'.format(port, ws_path)


@pytest.fixture(scope='session')
def playwright_instance():
    with sync_playwright() as p:
        yield p


@pytest.fixture(scope='session')
def cdp_browser(playwright_instance):
    try:
        # 直接连用户正在使用的 Chrome，这样能复用现有登录态
        browser = playwright_instance.chromium.connect_over_cdp(get_cdp_ws(), timeout=15000)
    except Exception as e:
        pytest.fail('连接 Chrome 失败，确认远程调试已经打开：{}'.format(e))

    yield browser
    browser.close()


@pytest.fixture
def device_page(cdp_browser):
    if not cdp_browser.contexts:
        pytest.fail('Chrome 里没有可用的浏览器上下文')

    page = cdp_browser.contexts[0].new_page()
    url = os.getenv('UI_DASHBOARD_URL', DEFAULT_DASHBOARD_URL)
    page.goto(url, wait_until='domcontentloaded', timeout=30000)

    ui = DevicePage(page)
    ui.wait_loaded()
    yield ui
    page.close()