import os
from datetime import datetime

from BeautifulReport import BeautifulReport

from common.HTMLTestRunner import HTMLTestRunner


def report(ts, filename, report_dir, theme='theme_default', title=None,
           description=None, tester=None, _type='br'):
    '''
    执行用例并生成报告
    :param ts: 测试套件
    :param filename: 报告文件名
    :param report_dir: 报告文件夹，仅支持BeautifulReport
    :param theme: 主题，仅支持BeautifulReport
    :param title: 报告标题，仅支持HTMLTestRunner
    :param description: 报告描述
    :param tester: 测试人员，仅支持HTMLTestRunner
    :param _type: 默认值为br，表示生成BeautifulReport风格的报告
    :return:
    '''

    # 1.生成时间前缀
    time_prefix = datetime.now().strftime('%Y%m%d%H%M%S')
    # 2.拼接时间前缀到报告文件名
    filename = '{}_{}'.format(time_prefix, filename)
    print('Report file name: {}'.format(filename))
    if _type == 'br':
        # 生成BeautifulReport报告
        br = BeautifulReport(ts)
        br.report(description=description, filename=filename, report_dir=report_dir, theme=theme)
    else:
        # 生成HTMLTestRunner报告
        with open(os.path.join(report_dir, filename), 'wb') as f:
            runner = HTMLTestRunner(f, title=title, description=description, tester=tester)
            runner.run(ts)