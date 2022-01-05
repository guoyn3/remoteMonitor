import pytest
import allure
from rm.api.rmProjectSnapshot import rmProjectSnapshot
from common.readJsonData import ReadJsonData


@allure.feature("功能点:对/api/gcp-rm/rmProjectSnapshot/findById接口进行测试")
@allure.title("{title}")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize("body,code,message,title", ReadJsonData(file="rmProjectSnapshot\\findById.json").getBody())
def test_create(get_session, body, code, message, title):
    res = rmProjectSnapshot(s=get_session).findById(body=body, code=code, message=message, title=title)
    res_code = res[0]
    res_message = res[1]
    assert res_code == str(code)
    assert res_message == message


@allure.feature("功能点:对/api/gcp-rm/rmProjectSnapshot/findProjectUser接口进行测试")
@allure.title("{title}")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize("body,code,message,title", ReadJsonData(file="rmProjectSnapshot\\findProjectUser.json").getBody())
def test_update(get_session, body, code, message, title):
    res = rmProjectSnapshot(s=get_session).findProjectUser(body=body, code=code, message=message, title=title)
    res_code = res[0]
    res_message = res[1]
    assert res_code == str(code)
    assert res_message == message


