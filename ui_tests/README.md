# UI 自动化测试

这套用例直接连当前正在使用的 Chrome，复用已有登录态，不会另开一个无登录的浏览器。

## 目录

```text
ui_tests/
├── conftest.py
├── pages/                   # 页面对象
│   ├── base_page.py
│   ├── device_page.py
│   ├── software_page.py
│   ├── upgrade_task_page.py
│   ├── upgrade_record_page.py
│   ├── device_log_page.py
│   ├── account_page.py
│   ├── department_page.py
│   ├── person_privilege_page.py
│   ├── member_list_page.py
│   ├── issue_result_page.py
│   ├── whitelist_page.py
│   ├── blacklist_page.py
│   ├── access_record_page.py
│   └── visitor_page.py
├── case_objects/            # 用例对象和参数化数据
│   ├── models.py
│   └── case_data.py
├── test_device_page.py
├── test_page_objects.py
├── test_filter_cases.py
├── test_drawer_cases.py
└── test_menu_cases.py
```

页面对象负责定位元素和常见操作，测试文件只负责组合步骤、做断言；`case_objects` 里的对象用来参数化页面检查、查询、菜单、抽屉等场景。

## 运行前

1. Chrome 打开 `chrome://inspect/#remote-debugging`，勾选允许远程调试。
2. 登录并打开 `http://172.168.80.54/dashboard/analysis`。
3. 安装依赖：`pip install -r requirements-ui.txt`

## 执行

```powershell
pytest ui_tests -v
```

如果地址或 Chrome profile 不一样，可以临时覆盖：

```powershell
$env:UI_DASHBOARD_URL="http://172.168.80.54/dashboard/analysis"
$env:UI_CHROME_PROFILE="C:\Users\你的用户名\AppData\Local\Google\Chrome\User Data"
pytest ui_tests -v
```

已有标准 CDP WebSocket 地址时，也可以直接设置 `UI_CDP_WS`。

## 当前页面对象

- 设备管理：通行设备、软件版本、升级任务、升级记录、设备日志
- 人员管理：部门管理、人员权限、人员列表、人员下发结果、白名单、黑名单
- 通行记录：门禁通行记录
- 访客管理
- 账号管理

## 当前用例覆盖

- 页面加载、主要按钮和表头检查
- 设备 SN/名称查询、空结果、重置和筛选列
- 人员权限、人员列表、下发结果、白名单、黑名单查询
- 门禁通行记录、访客、账号查询
- 人员管理、通行记录子菜单展开和链接检查
- 访客管理、账号管理入口检查
- 多页面跳转和返回
- 添加设备、添加用户、添加人员抽屉字段检查

涉及新增、删除、提交、升级等写操作的地方只检查打开和取消，不真正提交数据。