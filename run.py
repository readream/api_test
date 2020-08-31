import os
import pytest


from utils import function,common

project_path = function.project_path()
print(project_path)

if __name__ == '__main__':

    report_path = os.path.join(project_path, "report", "result")
    report_html_path = os.path.join(project_path, "report", "html")
    pytest.main(["-s", "--alluredir", report_path])
    common.allure_report(report_path, report_html_path)
    # common.send_mail()
    # os.system("D:/python/Lib/site-packages/allure-2.10.0/bin/allure.bat "
    #           "generate "
    #           "D:/learn/api_test/api_test/interfaceTest/report/result "
    #           "-o "
    #           "D:/learn/api_test/api_test/interfaceTest/report/html "
    #           "--clean")