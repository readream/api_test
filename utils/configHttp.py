import requests, json
from utils.function import ReadConfig, project_path
port = ReadConfig().get_http("port")
class configHttp():
    # 获取url配置相关信息/相关json/get/post方法定义
    def __init__(self):
        global  port ,timeout
        port = ReadConfig().get_http("port")
        timeout = ReadConfig().get_http("timeout")
        self.headers = {}
        self.params = {}
        self.data = {}
        self.url = None
        self.files = {}
        self.state = 0
    def set_url(self, url):
        scheme = ReadConfig().get_http("scheme")
        host = ReadConfig().get_http("baseurl")
        port = ReadConfig().get_http("port")
        self.url = scheme +'://'+host+":"+port+url
    def set_headers(self, header):
        self.headers = header
    def set_params(self, param):
        self.params = param
    def set_data(self, data):
        self.data = data
    def set_files(self, filename):
        if filename != '':
            file_path = project_path()+'data\\'+filename
            self.files = {'file': open(file_path,'rb')}
        else:
            self.state = 1
    #get方法封装
    def get(self):
        try:
            response = requests.get(self.url, headers=self.headers,parmas=self.params,timeout=float(timeout))
            return response
        except TimeoutError:
            print("Time out!")
            return None
    #post方法封装
    def post(self):
        try:
            response = requests.post(self.url, headers=self.headers, data=self.data,timeout=float(timeout))
            return response
        except TimeoutError:
            print("Time out!")
            return None

    # 定义post上传方法
    def postWithFile(self):
        try:
            response = requests.post(self.url, headers=self.headers, data=self.data, files=self.files,
                                         timeout=float(timeout))
            return response
        except TimeoutError:
            print("Time out!")
            return None

    # 定义请求post json格式方法
    def postWithJson(self):
        try:
            response = requests.post(self.url, headers=self.headers, data=json.dumps(self.data), timeout=float(timeout))
            return response
        except TimeoutError:
            print("Time out!")
            return None

if __name__ == "__main__":
    pass
