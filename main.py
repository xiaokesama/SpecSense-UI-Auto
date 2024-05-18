import unittest

from common.report_handler import report

import settings

if __name__ == '__main__':
    ts = unittest.TestLoader().discover('testcases')
    report(ts, **settings.REPORT_CONFIG)
