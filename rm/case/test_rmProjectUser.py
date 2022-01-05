import pytest
import allure
from rm.api.rmProjectUser import rmProjectUser
from common.readJsonData import ReadJsonData


@allure.feature("功能点:对/api/gcp-rm/rmProjectUser/batchCreate接口进行测试")
@allure.title("纳入用户")
@allure.severity(allure.severity_level.NORMAL)
def test_batchCreate(get_session):
    res = rmProjectUser(s=get_session).batchCreate()
    res_code = res[0]
    res_message = res[1]
    assert res_code == "0"
    assert res_message == "成功!"


@allure.feature("功能点:对/api/gcp-rm/rmProjectUser/batchDelete接口进行测试")
@allure.title("{title}")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize("body,code,message,title", ReadJsonData(file="rmProjectUser\\batchDelete.json").getBody())
def test_batchDelete(get_session, body, code, message, title):
    res = rmProjectUser(s=get_session).batchDelete(body=body, code=code, message=message, title=title)
    res_code = res[0]
    res_message = res[1]
    assert res_code == str(code)
    assert res_message == message


@allure.feature("功能点:对/api/gcp-rm/rmProjectUser/checkUserProject接口进行测试")
@allure.title("{title}")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize("body,code,message,title", ReadJsonData(file="rmProjectUser\\checkUserProject.json").getBody())
def test_checkUserProject(get_session, body, code, message, title):
    res = rmProjectUser(s=get_session).checkUserProject(body=body, code=code, message=message, title=title)
    res_code = res[0]
    res_message = res[1]
    assert res_code == str(code)
    assert res_message == message


@allure.feature("功能点:对/api/gcp-rm/rmProjectUser/findUserProjectCount接口进行测试")
@allure.title("{title}")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize("body,code,message,title", ReadJsonData(file="rmProjectUser\\findUserProjectCount.json").getBody())
def test_findUserProjectCount(get_session, body, code, message, title):
    res = rmProjectUser(s=get_session).findUserProjectCount(body=body, code=code, message=message, title=title)
    res_code = res[0]
    res_message = res[1]
    assert res_code == str(code)
    assert res_message == message


@allure.feature("功能点:对/api/gcp-rm/rmProjectUser/findProjectUser接口进行测试")
@allure.title("{title}")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize("body,code,message,title", ReadJsonData(file="rmProjectUser\\findProjectUser.json").getBody())
def test_findProjectUser(get_session, body, code, message, title):
    res = rmProjectUser(s=get_session).findProjectUser(body=body, code=code, message=message, title=title)
    res_code = res[0]
    res_message = res[1]
    assert res_code == str(code)
    assert res_message == message
