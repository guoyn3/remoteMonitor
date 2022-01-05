import pytest
import allure
from rm.api.rmUser import rmUser
from common.readJsonData import ReadJsonData


@allure.feature("功能点：对/api/gcp-rm/rmUser/createOrUpdate接口进行测试")
@allure.title("{title}")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize("body,code,message,title", ReadJsonData(file="rmUser\\createOrUpdate.json").getBody())
def test_createOrUpdate(get_session, body, code, message, title):
    res = rmUser(s=get_session).createOrUpdate(body=body, code=code, message=message)
    res_code = res[0]
    res_message = res[1]
    assert res_code == str(code)
    assert res_message == message


@allure.feature("功能点：对/api/gcp-rm/rmUser/findById接口进行测试")
@allure.title("{title}")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize("body,code,message,title", ReadJsonData(file="rmUser\\findById.json").getBody())
def test_findById(get_session, body, code, message, title):
    res = rmUser(s=get_session).findById(body=body, code=code, message=message)
    res_code = res[0]
    res_message = res[1]
    assert res_code == str(code)
    assert res_message == message


@allure.feature("功能点：对/api/gcp-rm/rmUser/findByPage接口进行测试")
@allure.title("{title}")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize("body,code,message,title", ReadJsonData(file="rmUser\\findByPage.json").getBody())
def test_findByPage(get_session, body, code, message, title):
    res = rmUser(s=get_session).findByPage(body=body, code=code, message=message)
    res_code = res[0]
    res_message = res[1]
    assert res_code == str(code)
    assert res_message == message


@allure.feature("功能点：对/api/gcp-rm/rmUser/findUser接口进行测试")
@allure.title("{title}")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize("body,code,message,title", ReadJsonData(file="rmUser\\findUser.json").getBody())
def test_findUser(get_session, body, code, message, title):
    res = rmUser(s=get_session).findUser(body=body, code=code, message=message)
    res_code = res[0]
    res_message = res[1]
    assert res_code == str(code)
    assert res_message == message
