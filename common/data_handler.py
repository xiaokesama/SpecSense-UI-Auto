import json
import random
from openpyxl import load_workbook
import re


def get_test_data_from_excel(file,sheet_name) -> list:
    # 读取excel文件
    wb = load_workbook(file)
    sh = wb[sheet_name]
    row = sh.max_row
    column = sh.max_column
    for i in range(1,1000000):
        if sh.cell(row=i,column=1).value is None:
            row = i-1
            break
    for i in range(1,1000000):
        if sh.cell(row=1,column=i).value is None:
            column = i-1
            break

    # 存储数据
    data = []
    keys = []

    # 第一行
    for i in range(1,column+1):
        keys.append(sh.cell(row=1,column=i).value)

    for i in range(2,row+1):
        temp = {}
        for j in range(1,column+1):
            temp[keys[j-1]]=sh.cell(row=i,column=j).value
        data.append(temp)

    # 后续行
    # for i in range(2,row+1):
    #     temp = {}
    #     for j in range(1,column+1):
    #         temp[keys[j-1]]=sh.cell(row=i,column=j).value
    #     try:
    #         temp['request']=json.loads(temp['request'])
    #         temp['expect_data']=json.loads(temp['expect_data'])
    #     except json.decoder.JSONDecodeError:
    #         raise ValueError("用例数据格式错误，请检查request和expect_data是否为json格式")
    #     data.append(temp)
    return data


def generate_phone():
    phone = '1' + str(random.randint(3,9)) + str(random.randint(3,9))
    for i in range(8):
        phone += str(i)
    return phone


def replace_args_by_re(json_s, obj):
    '''
    通过正则表达式动态的替换参数
    :param json_s:包含替换内容的数据
    :param obj:
    :return:
    '''
    # 1.找出所有的槽位中的变量名(若公司项目中#为特殊字符，可将用例和此次#替换为其他特殊符号
    args = re.findall('#(.*?)#', json_s)

    for arg in args:
        # 2.找到obj中对应的属性,若无对应的属性，则返回None
        value = getattr(obj, arg, None)
        if value:
            json_s = json_s.replace('#{}#'.format(arg), str(value))
    return json_s



if __name__ == '__main__':
    file = '../test_data/test_data.xlsx'
    sheet_name = 'register'
    data = get_test_data_from_excel(file,sheet_name)
    print(data)
    print(type(data[0]))
    print(data[0].get('id'))
    print(type(data))
