# 在common文件夹下新建fixture.py文件
import requests

import settings
from common import logger
from common.utils import url_join


# 名称定义为_type可以避免与python中关键参数冲突
def register(mobilephone, pwd, reg_name=None, _type=None):
    '''
    注册用户
    :param mobile_phone: 电话号码
    :param pwd: 密码
    :param reg_name: 昵称
    :param _type: 类型
    :return:
    '''
    # 1.构造发送注册请求的参数
    data = {
        'mobilephone': mobilephone,
        'pwd': pwd
    }
    if reg_name:
        data['reg_name'] = reg_name
    # 使用if _type:进行判断时，传值为0，无法传入，故判断不为空
    if _type is not None:
        data['type'] = _type
    headers = {"x-Lemonban-Media-Type": "lemonban.v2"}
    url = url_join(settings.PROJECT_HOST, settings.INTERFACES['register'])
    try:
        res = requests.post(url=url, data=data, headers=headers)
        if res.json()['msg'] == '注册成功':
            logger.info('注册用户成功')
            return True
        return False
    except Exception as e:
        logger.exception('注册用户失败')
        raise e


def login(mobilephone, pwd):
    '''
    登录用户
    :param mobilephone: 用户手机号
    :param pwd: 用户密码
    :return:
    '''
    # 构造请求数据
    data = {
        'mobilephone': mobilephone,
        'pwd': pwd
    }
    headers = {'x-Lemonban-Media-Type': 'lemonban.v2'}

    url = url_join(settings.PROJECT_HOST, settings.INTERFACES['login'])
    try:
        res = requests.post(url=url, data=data, headers=headers)
        if res.json()['msg'] == '登录成功':
            logger.info('登录用户成功')
            return res.json()
    except Exception as e:
        logger.exception('登录用户失败')
        raise e


def add_loan(member_id, token, title='借钱实现财富自由', amount=5000,
             loan_rate=12.0, loan_term=3, loan_date_type=1, bidding_days=5):
    """
    添加一个项目
    :param member_id:
    :param token:
    :param title:
    :param amount:
    :param loan_rate:
    :param loan_term:
    :param loan_date_type:
    :param bidding_days:
    :return:
    """
    data = {
        'member_id': member_id,
        'title': title,
        'amount': amount,
        'loan_rate': loan_rate,
        'loan_term': loan_term,
        'loan_date_type': loan_date_type,
        'bidding_days': bidding_days,
    }
    headers = {"X-Lemonban-Media-Type": "lemonban.v2", "Authorization": token}
    url = url_join(settings.PROJECT_HOST, settings.INTERFACES['add'])
    try:
        res = requests.post(url=url, json=data, headers=headers)
        if res.status_code == 200:
            logger.info('创建项目成功')
            return res.json()['data']
    except Exception as e:
        logger.exception('创建项目失败')
    raise e


if __name__ == '__main__':
    from common.data_handler import generate_phone

    phone = generate_phone()
    pwd = '123456'
    register_res = register(mobilephone=phone, pwd=pwd)
    if register_res:
        login_res = login(mobilephone=phone, pwd=pwd)
        print(login_res)
    else:
        print('注册失败')