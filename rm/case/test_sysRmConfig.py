import pytest
import allure
from rm.api.sysRmConfig import sysRmConfig
from common.readJsonData import ReadJsonData


@allure.feature("功能点：对/api/gcp-rm/sysRmConfig/findProjectMonitor接口进行测试")
@allure.title("获取远程监查配置成功")
@allure.severity(allure.severity_level.NORMAL)
def test_findProjectMonitor(get_session):
    res = sysRmConfig(s=get_session).findProjectMonitor()
    res_code = res[0]
    assert res_code == "0"


@allure.feature("功能点：对/api/gcp-rm/sysRmConfig/findSubjectMonitor接口进行测试")
@allure.title("获取受试者审批配置成功")
@allure.severity(allure.severity_level.NORMAL)
def test_findSubjectMonitor(get_session):
    res = sysRmConfig(s=get_session).findSubjectMonitor()
    res_code = res[0]
    assert res_code == "0"


@allure.feature("功能点：对/api/gcp-rm/sysRmConfig/update接口进行测试")
@allure.title("{title}")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize("body,code,message,title",ReadJsonData(file="sysRmConfig\\update.json").getBody())
def test_update(get_session,body,code,message,title):
    res = sysRmConfig(s=get_session).update(body=body, code=code, message=message, title=title)
    res_code = res[0]
    res_message = res[1]
    assert res_code == str(code)
    assert res_message == message
