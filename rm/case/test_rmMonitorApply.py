import pytest
import allure
from rm.api.rmMonitorApply import rmMonitorApply
from common.readJsonData import ReadJsonData
from common.connectMysql import ConnectMysql

@allure.feature("功能点:对/api/gcp-rm/rmMonitorApply/canApply接口进行测试")
@allure.title("{title}")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize("body,code,message,title", ReadJsonData(file="rmMonitorApply\\canApply.json").getBody())
def test_canApply(get_session, body, code, message, title):
    res = rmMonitorApply(s=get_session).canApply(body=body, code=code, message=message, title=title)
    res_code = res[0]
    res_message = res[1]
    assert res_code == str(code)
    assert res_message == message


@allure.feature("功能点:对/api/gcp-rm/rmMonitorApply/create接口进行测试")
@allure.title("添加远程监查申请")
@allure.severity(allure.severity_level.NORMAL)
def test_create(get_session):
    res = rmMonitorApply(s=get_session).create()
    res_code = res[0]
    res_message = res[1]
    assert res_code == "0"
    assert res_message == "成功!"


@allure.feature("功能点:对/api/gcp-rm/rmMonitorApply/findById接口进行测试")
@allure.title("{title}")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize("body,code,message,title", ReadJsonData(file="rmMonitorApply\\findById.json").getBody())
def test_findById(get_session, body, code, message, title):
    res = rmMonitorApply(s=get_session).findById(body=body, code=code, message=message, title=title)
    res_code = res[0]
    res_message = res[1]
    assert res_code == str(code)
    assert res_message == message


@allure.feature("功能点:对/api/gcp-rm/rmMonitorApply/findByPage接口进行测试")
@allure.title("{title}")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize("body,code,message,title", ReadJsonData(file="rmMonitorApply\\findByPage.json").getBody())
def test_findByPage(get_session, body, code, message, title):
    res = rmMonitorApply(s=get_session).findByPage(body=body, code=code, message=message, title=title)
    res_code = res[0]
    res_message = res[1]
    assert res_code == str(code)
    assert res_message == message


@allure.feature("功能点:对/api/gcp-rm/rmMonitorApply/getMonitorStype接口进行测试")
@allure.title("获取受试者监查类型枚举成功")
@allure.severity(allure.severity_level.NORMAL)
def test_getMonitorStype(get_session):
    res = rmMonitorApply(s=get_session).getMonitorStype()
    res_code = res[0]
    assert res_code == "0"


@allure.feature("功能点:对/api/gcp-rm/rmMonitorApply/undoneMonitorApply接口进行测试")
@allure.title("撤销远程监查申请通过")
@allure.severity(allure.severity_level.NORMAL)
def test_undoneMonitorApply(get_session,get_rmApprovalId):
    res = rmMonitorApply(s=get_session).undoneMonitorApply(id=get_rmApprovalId)
    res_code = res[0]
    assert res_code == "0"


@allure.feature("功能点:对/api/gcp-rm/rmMonitorApply/update接口进行测试")
@allure.title("{title}")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize("body,code,message,title", ReadJsonData(file="rmMonitorApply\\update.json").getBody())
def test_update(get_session, body, code, message, title):
    res = rmMonitorApply(s=get_session).update(body=body, code=code, message=message, title=title)
    res_code = res[0]
    res_message = res[1]
    assert res_code == str(code)
    assert res_message == message






