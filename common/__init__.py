# 这个点是相对于main.py的路径的
from common.log_handler import get_logger
from common.config_handler import get_config
from common.db_handler import DB
from common.report_handler import report
import settings
import os

# 单例模式，只给向外供给调用
logger=get_logger(
    name=settings.LOG_CONFIG['name'],
    filename=os.path.join(settings.ROOT_PATH,settings.LOG_CONFIG['filename']),
    debug=settings.LOG_CONFIG['debug']
)

# 数据库连接
db=DB(settings.DB_CONFIG)







