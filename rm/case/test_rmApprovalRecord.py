import pytest
import allure
from rm.api.rmApprovalRecord import rmApprovalRecord
from common.readJsonData import ReadJsonData


@allure.feature("功能点:对/api/gcp-rm/rmApprovalRecord/create接口进行测试")
@allure.title("{title}")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize("body, code, message, title", ReadJsonData(file="rmApprovalRecord\\create.json").getBody())
def test_create(get_session, body, code, message, title):
    res = rmApprovalRecord(s=get_session).create(body=body, code=code, message=message, title=title)
    res_code = res[0]
    res_message = res[1]
    assert res_code == str(code)
    assert res_message == message


@allure.feature("功能点:对/api/gcp-rm/rmApprovalRecord/deleteById接口进行测试")
@allure.title("删除审批记录")
@allure.severity(allure.severity_level.NORMAL)
def test_deleteById(get_session,get_rmApprovalRecordId):
    res = rmApprovalRecord(s=get_session).deleteById(id="")
    res_code = res[0]
    res_message = res[1]
    assert res_code == "0"
    assert res_message == "成功!"


@allure.feature("功能点:对/api/gcp-rm/rmApprovalRecord/findByPage接口进行测试")
@allure.title("{title}")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize("body, code, message, title", ReadJsonData(file="rmApprovalRecord\\findByPage.json").getBody())
def test_findByPage(get_session, body, code, message, title):
    res = rmApprovalRecord(s=get_session).findByPage(body=body, code=code, message=message, title=title)
    res_code = res[0]
    res_message = res[1]
    assert res_code == str(code)
    assert res_message == message


@allure.feature("功能点:对/api/gcp-rm/rmApprovalRecord/update接口进行测试")
@allure.title("{title}")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize("body, code, message, title", ReadJsonData(file="rmApprovalRecord\\update.json").getBody())
def test_update(get_session, body, code, message, title):
    res = rmApprovalRecord(s=get_session).update(body=body, code=code, message=message, title=title)
    res_code = res[0]
    res_message = res[1]
    assert res_code == str(code)
    assert res_message == message












