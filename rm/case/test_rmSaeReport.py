import pytest
import allure
from rm.api.rmSaeReport import rmSaeReport
from common.readJsonData import ReadJsonData


@allure.feature("功能点:对/api/gcp-rm/rmSaeReport/create接口进行测试")
@allure.title("{title}")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize("body,code,message,title", ReadJsonData(file="rmSaeReport\\create.json").getBody())
def test_create(get_session, body, code, message, title):
    res = rmSaeReport(s=get_session).create(body=body, code=code, message=message, title=title)
    res_code = res[0]
    res_message = res[1]
    assert res_code == str(code)
    assert res_message == message


@allure.feature("功能点:对/api/gcp-rm/rmSaeReport/deleteById接口进行测试")
@allure.title("{title}")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize("body,code,message,title", ReadJsonData(file="rmSaeReport\\deleteById.json").getBody())
def test_deleteById(get_session, body, code, message, title):
    res = rmSaeReport(s=get_session).deleteById(body=body, code=code, message=message, title=title)
    res_code = res[0]
    res_message = res[1]
    assert res_code == str(code)
    assert res_message == message


@allure.feature("功能点:对/api/gcp-rm/rmSaeReport/findByPage接口进行测试")
@allure.title("{title}")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize("body,code,message,title", ReadJsonData(file="rmSaeReport\\findByPage.json").getBody())
def test_findByPage(get_session, body, code, message, title):
    res = rmSaeReport(s=get_session).findByPage(body=body, code=code, message=message, title=title)
    res_code = res[0]
    res_message = res[1]
    assert res_code == str(code)
    assert res_message == message


@allure.feature("功能点:对/api/gcp-rm/rmSaeReport/update接口进行测试")
@allure.title("{title}")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize("body,code,message,title", ReadJsonData(file="rmSaeReport\\update.json").getBody())
def test_update(get_session, body, code, message, title):
    res = rmSaeReport(s=get_session).update(body=body, code=code, message=message, title=title)
    res_code = res[0]
    res_message = res[1]
    assert res_code == str(code)
    assert res_message == message
