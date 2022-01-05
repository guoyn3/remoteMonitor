import pytest
import allure
from rm.api.rmProjectLog import rmProjectLog
from common.readJsonData import ReadJsonData


@allure.feature("功能点:对/api/gcp-rm/rmProjectLog/create接口进行测试")
@allure.title("{title}")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize("body,code,message,title", ReadJsonData(file="rmProjectLog\\create.json").getBody())
def test_create(get_session, body, code, message, title):
    res = rmProjectLog(s=get_session).create(body=body, code=code, message=message, title=title)
    res_code = res[0]
    res_message = res[1]
    assert res_code == str(code)
    assert res_message == message


@allure.feature("功能点:对/api/gcp-rm/rmProjectLog/deleteById接口进行测试")
@allure.title("{title}")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize("body,code,message,title", ReadJsonData(file="rmProjectLog\\deleteById.json").getBody())
def test_deleteById(get_session, body, code, message, title):
    res = rmProjectLog(s=get_session).deleteById(body=body, code=code, message=message, title=title)
    res_code = res[0]
    res_message = res[1]
    assert res_code == str(code)
    assert res_message == message


@allure.feature("功能点:对/api/gcp-rm/rmProjectLog/update接口进行测试")
@allure.title("{title}")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize("body,code,message,title", ReadJsonData(file="rmProjectLog\\update.json").getBody())
def test_update(get_session, body, code, message, title):
    res = rmProjectLog(s=get_session).update(body=body, code=code, message=message, title=title)
    res_code = res[0]
    res_message = res[1]
    assert res_code == str(code)
    assert res_message == message


@allure.feature("功能点:对/api/gcp-rm/rmProjectLog/findById接口进行测试")
@allure.title("{title}")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize("body,code,message,title", ReadJsonData(file="rmProjectLog\\findById.json").getBody())
def test_findById(get_session, body, code, message, title):
    res = rmProjectLog(s=get_session).findById(body=body, code=code, message=message, title=title)
    res_code = res[0]
    res_message = res[1]
    assert res_code == str(code)
    assert res_message == message


@allure.feature("功能点:对/api/gcp-rm/rmProjectLog/findByPage接口进行测试")
@allure.title("{title}")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize("body,code,message,title", ReadJsonData(file="rmProjectLog\\findByPage.json").getBody())
def test_findByPage(get_session, body, code, message, title):
    res = rmProjectLog(s=get_session).findByPage(body=body, code=code, message=message, title=title)
    res_code = res[0]
    res_message = res[1]
    assert res_code == str(code)
    assert res_message == message


@allure.feature("功能点:对/api/gcp-rm/rmProjectLog/listAllByProjectId接口进行测试")
@allure.title("{title}")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize("body,code,message,title", ReadJsonData(file="rmProjectLog\\listAllByProjectId.json").getBody())
def test_listAllByProjectId(get_session, body, code, message, title):
    res = rmProjectLog(s=get_session).listAllByProjectId(body=body, code=code, message=message, title=title)
    res_code = res[0]
    res_message = res[1]
    assert res_code == str(code)
    assert res_message == message



