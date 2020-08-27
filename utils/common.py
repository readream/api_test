import xlrd
import os
import subprocess
from utils.function import ReadConfig
import json, requests
from utils.send_email import SendEmail
from utils.log import Logg
from utils.function import project_path
from config import excelConfig


log = Logg().get_logger()
data = excelConfig.DataConfig
project_path=project_path()
def get_xls(xls_name, sheet_name):
    cls = []
    xlsPath = os.path.join(project_path,'data',xls_name)
    file = xlrd.open_workbook(xlsPath)
    sheet = file.sheet_by_name(sheet_name)
    nrows = sheet.nrows
    title = sheet.row_values(0)
    for i in range(1,nrows):
        cls.append(dict(zip(title, sheet.row_values(i))))
    return cls
# 获取token
def get_token():
    send_param = {"username": "python", "password": "12345678"}
    urllist = ReadConfig().get_http("BASEURL")
    headers = {"Content-Type": 'application/json'}
    res = requests.post("http://" + urllist + ":8064"+"/authorizations/", data=json.dumps(send_param),headers=headers)
    info = res.json()
    # print(info['token'])
    # header中获取token
    token = info['token']
    print(res.url)
    print(type(str(res.status_code)))
    # logger=log.get_logger()
    # logger.debug("Create token:%s" % (token))
    return res
#报告返回接口信息信息公共方法
def show_return_msg(response):
    # 返回response返回信息
    url = response.url
    # 返回json返回值
    msg = response.text
    print("\n请求地址：" + url)
    # 可以显示中文
    print("\n请求返回值：" + '\n' + json.dumps(json.loads(msg), ensure_ascii=False, sort_keys=True, indent=4))
def allure_report(report_path,report_html):
    """
    生成allure 报告
    :param report_path:
    :param report_html:
    :return:
    """
    #执行命令 allure generate
    allure_cmd ="allure generate %s -o %s --clean"%(report_path,report_html)
    #subprocess.call
    log.info("报告地址")
    try:
        subprocess.call(allure_cmd,shell=True)
    except:
        log.error("执行用例失败，请检查一下测试环境相关配置")
        raise
def send_mail(report_html_path="",content="",title="测试"):
    """
    发送邮件
    :param report_html_path:
    :param content:
    :param title:
    :return:
    """
    smtp_addr = ReadConfig().get_email("smtpserver")
    username = ReadConfig().get_email("username")
    password = ReadConfig().get_email("password")
    recv = ReadConfig().get_email("receiver")
    email = SendEmail(
        smtp_addr=smtp_addr,
        username=username,
        password=password,
        recv=recv,
        title=title,
        content=content,
        file=report_html_path)
    email.send_mail()
if __name__ == '__main__':
    # print(get_xls("testdata.xlsx", "美多商城接口测试"))
    # print(get_token())
    # show_return_msg(get_token())
    # print(project_path)
    send_mail()
