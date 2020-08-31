import os, configparser, re
p_data = '\${(.*)}\$'
# 获取项目路径
def project_path():
    return os.path.abspath(os.path.dirname(__file__)).split('utils')[0]
configPath = project_path()+'config.ini'

def res_find(data,pattern_data=p_data):
    """
    查询
    :param data:
    :param pattern_data:
    :return:
    """
    #pattern = re.compile('\${(.*)}\$')
    pattern = re.compile(pattern_data)
    re_res = pattern.findall(data)
    return re_res

def res_sub(data,replace,pattern_data=p_data):
    """
    替换
    :param data:
    :param replace:
    :param pattern_data:
    :return:
    """
    pattern = re.compile(pattern_data)
    re_res = pattern.findall(data)
    if re_res:
        return re.sub(pattern_data,replace,data)
    return data

def params_find(headers,cookies):
    """
    验证请求中是否有${}$需要结果关联
    :param headers:
    :param cookies:
    :return:
    """
    if "${" in headers:
        headers = res_find(headers)
    if "${" in cookies:
        cookies = res_find(cookies)
    return headers,cookies
class ReadConfig():
    def __init__(self):
        # 创建对象
        self.cf = configparser.ConfigParser()
        #读取config.ini路径
        self.cf.read(configPath)
    # 获取对应配置信息
    def get_http(self, name):
        value = self.cf.get('HTTP', name)
        return value
    def get_email(self, name):
        value = self.cf.get('email', name)
        return value
if __name__ == '__main__':
    pass