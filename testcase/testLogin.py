import allure, json, os
from config import excelConfig
from utils import common, configHttp, log,function
import pytest
student_xls = common.get_xls('testdata.xlsx', '美多商城接口测试')
log = log.Logg()
configHttp = configHttp.configHttp()
project_path = function.project_path()
print(project_path)
data_key = excelConfig.DataConfig
#参数化
class TestLogin():
    @pytest.mark.parametrize("data", student_xls)
    def test_login(self, data):
        '''学生端登陆'''
        self.url = data[data_key.url]
        self.parameter = json.loads(data[data_key.params])
        self.status_code = data[data_key.code]
        self.case_model = data[data_key.case_model]
        self.case_id = data[data_key.case_id]
        self.case_name = data[data_key.case_name]
        self.method = data[data_key.method]
        self.expect_result = data[data_key.expect_result]
        configHttp.set_url(self.url)
        header = {"Content-Type": 'application/json'}
        configHttp.set_headers(header)
        print(configHttp.set_data(self.parameter))
        # 请求对应封装接口
        self.respon = configHttp.postWithJson()
        print(self.respon.text)
        # allure
        # sheet名称  feature 一级标签
        allure.dynamic.feature("接口测试")
        # 模块   story 二级标签
        allure.dynamic.story(self.case_model)
        # 用例ID+接口名称  title
        allure.dynamic.title(self.case_id + self.case_name)
        # 请求URL  请求类型 期望结果 实际结果描述
        desc = "<font color='red'>请求URL: </font> {}<Br/>" \
               "<font color='red'>请求类型: </font>{}<Br/>" \
               "<font color='red'>期望结果: </font>{}<Br/>" \
               "<font color='red'>实际结果: </font>{}".format(self.url, self.method, self.expect_result, self.respon)
        allure.dynamic.description(desc)
        assert self.status_code == str(self.respon.status_code)
        # 调用checkResult方法
        self.checkResult()

    def setUp(self):
        # 初始化
        logger = log.get_logger()
        logger.info("登录")

    # 较验json格式返回值
    def checkResult(self):
        common.show_return_msg(self.respon)


if __name__ == '__main__':
    # pytest.main(["-s","testLogin.py"])
    pytest.main(['-s','testLogin.py'])
