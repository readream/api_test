import os, configparser
# 获取项目路径
def project_path():
    return os.path.abspath(os.path.dirname(__file__)).split('utils')[0]
configPath = project_path()+'config.ini'
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
    print(ReadConfig().get_email("password"))