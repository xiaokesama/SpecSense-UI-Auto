from ui_tests.case_objects.models import ColumnCase, DrawerCase, FilterCase, MenuGroupCase, PageCase, SearchCase


PAGE_CASES = (
    PageCase(
        'device_page',
        '通行设备页主要控件检查',
        'device',
        ('查询', '重置', '添加设备', '批量导入', '导出', '筛选列'),
        ('应用版本', '固件版本', '设备名称', 'SN号', '操作'),
    ),
    PageCase(
        'software_page',
        '软件版本页主要控件检查',
        'software',
        ('更新版本', '添加下级', '批量删除', '查询', '重置', '软件版本上传'),
        ('设备类型', '设备机型', '设备方案', '应用版本', '文件名', '操作'),
    ),
    PageCase(
        'upgrade_task_page',
        '升级任务页主要控件检查',
        'upgrade_task',
        ('查询', '重置'),
        ('任务名称', '固件名称', '任务状态', '操作'),
    ),
    PageCase(
        'upgrade_record_page',
        '升级记录页主要控件检查',
        'upgrade_record',
        ('点击上传', '批量重试', '查询', '重置'),
        ('标识号(SN号)', '设备类型', '账号归属', '响应结果', '操作'),
    ),
    PageCase(
        'device_log_page',
        '设备日志页主要控件检查',
        'device_log',
        ('查询', '重置'),
        ('设备SN', '系统模块', '操作类型', '操作人员', '操作状态'),
    ),
    PageCase(
        'department_page',
        '部门管理页主要控件检查',
        'department',
        ('更新部门', '添加分组', '添加下级', '批量删除', '树操作'),
        (),
        False,
    ),
    PageCase(
        'person_privilege_page',
        '人员权限页主要控件检查',
        'person_privilege',
        ('查询', '重置', '下发到指定平板', '批量删除人员'),
        ('设备名称', 'SN码', '在线状态', '激活状态', '最近激活时间', '操作'),
    ),
    PageCase(
        'member_list_page',
        '人员列表页主要控件检查',
        'member_list',
        ('更新部门', '树操作', '查询', '重置', '添加人员', '导出', '批量导入', '筛选列'),
        ('注册照片', '姓名', '身份证', '性别', '电话号码', '卡号', '操作'),
    ),
    PageCase(
        'issue_result_page',
        '人员下发结果页主要控件检查',
        'issue_result',
        ('查询', '重置', '补下发'),
        ('注册头像', '人员姓名', '设备名称', '标识号(SN号)', '注册时间', '下发状态'),
    ),
    PageCase(
        'whitelist_page',
        '白名单页主要控件检查',
        'whitelist',
        ('查询', '重置'),
        ('注册照片', '姓名', '身份证', '性别', '电话号码', '卡号', '人员类型', '名单类型'),
    ),
    PageCase(
        'blacklist_page',
        '黑名单页主要控件检查',
        'blacklist',
        ('查询', '重置'),
        ('注册照片', '姓名', '身份证', '性别', '电话号码', '卡号', '人员类型', '名单类型'),
    ),
    PageCase(
        'access_record_page',
        '门禁通行记录页主要控件检查',
        'access_record',
        ('查询', '重置', '导出'),
        ('设备名称', '设备编号', '抓拍图', '人员姓名', '人员类型', 'IC卡号', '通行时间'),
    ),
    PageCase(
        'visitor_page',
        '访客管理页主要控件检查',
        'visitor',
        ('查询', '重置', '下发到指定平板'),
        ('照片', '姓名', '身份证', '操作'),
    ),
    PageCase(
        'account_page',
        '账号管理页主要控件检查',
        'account',
        ('查询', '重置', '添加用户'),
        ('账号', '名称', '手机号码', '创建时间', '操作'),
    ),
)


DEVICE_SEARCH_CASES = (
    SearchCase(
        'device_search_hit',
        '按已有SN查询设备',
        '2102233',
        False,
    ),
    SearchCase(
        'device_search_empty',
        '按不存在的SN查询设备',
        'AUTO_TEST_NO_SUCH_SN',
        True,
    ),
)


DEVICE_COLUMN_CASE = ColumnCase(
    'device_column_filter',
    '设备列表筛选列字段检查',
    ('全选', '设备名称', 'SN号', '应用版本', '设备状态', '操作'),
)


DEVICE_DRAWER_CASE = DrawerCase(
    'device_add_drawer',
    '添加设备抽屉字段检查',
    'device',
    '添加设备',
    '新增',
    ('请输入设备名称', '请输入SN号'),
)


DRAWER_CASES = (
    DEVICE_DRAWER_CASE,
    DrawerCase(
        'account_add_drawer',
        '添加用户抽屉字段检查',
        'account',
        '添加用户',
        '新增',
        (
            '请输入用户账号',
            '请输入登录密码',
            '请重新输入登录密码',
            '请输入用户名称',
            '请输入手机号码',
        ),
    ),
    DrawerCase(
        'member_add_drawer',
        '添加人员抽屉字段检查',
        'member_list',
        '添加人员',
        '新增',
        (
            '姓名',
            '请点击选择分组',
            '身份证',
            '请输入手机号码',
            '请输入卡号',
            '请输入籍贯',
            '请选择生日',
            '住址',
        ),
    ),
)


FILTER_CASES = (
    FilterCase(
        'software_name_filter',
        '软件版本按名称查询',
        'software',
        'search_by_name',
        '门禁',
    ),
    FilterCase(
        'upgrade_task_filter',
        '升级任务按任务名查询',
        'upgrade_task',
        'search_by_task',
        'FaceGate',
    ),
    FilterCase(
        'upgrade_record_filter',
        '升级记录按SN查询',
        'upgrade_record',
        'search_by_sn',
        '2102233',
    ),
    FilterCase(
        'device_log_filter',
        '设备日志按操作人员查询',
        'device_log',
        'search_by_operator',
        '系统管理员1',
    ),
    FilterCase(
        'person_privilege_filter',
        '人员权限按设备名称查询',
        'person_privilege',
        'search_by_device',
        '门禁',
    ),
    FilterCase(
        'member_list_filter',
        '人员列表按姓名查询',
        'member_list',
        'search_by_name',
        '1234',
    ),
    FilterCase(
        'issue_result_filter',
        '人员下发结果按姓名查询',
        'issue_result',
        'search_by_name',
        '1234',
    ),
    FilterCase(
        'whitelist_filter',
        '白名单按姓名查询',
        'whitelist',
        'search_by_name',
        '1234',
    ),
    FilterCase(
        'blacklist_filter',
        '黑名单按姓名查询',
        'blacklist',
        'search_by_name',
        'AUTO_TEST_NO_SUCH_MEMBER',
    ),
    FilterCase(
        'access_record_filter',
        '门禁通行记录按人员姓名查询',
        'access_record',
        'search_by_person',
        '1234',
    ),
    FilterCase(
        'visitor_filter',
        '访客管理按姓名查询',
        'visitor',
        'search_by_name',
        'AUTO_TEST_VISITOR',
    ),
    FilterCase(
        'account_name_filter',
        '账号管理按名称查询',
        'account',
        'search_by_name',
        '管理员',
    ),
)

MENU_GROUP_CASES = (
    MenuGroupCase(
        'personnel_menu',
        '人员管理菜单链接检查',
        '人员管理',
        (
            ('部门管理', '/isystem/depart'),
            ('人员权限', '/member/privilagelist'),
            ('人员列表', '/member/memberlist'),
            ('人员下发结果', '/member/issurelist'),
            ('白名单', '/member/whitelist'),
            ('黑名单', '/member/blacklist'),
        ),
    ),
    MenuGroupCase(
        'access_menu',
        '通行记录菜单链接检查',
        '通行记录',
        (
            ('门禁通行记录', '/current/accesslist'),
        ),
    ),
)