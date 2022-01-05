import pytest
import allure
from rm.api.rmMessage import rmMessage
from common.readJsonData import ReadJsonData


@allure.feature("功能点:对/api/gcp-rm/rmMessage/findByPage接口进行全量测试")
@allure.title("{title}")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize("body,code,message,title",ReadJsonData(file="rmMessage\\findByPage.json").getBody())
def test_FindByPage(get_session,body,code,message,title):
    res = rmMessage(s=get_session).findByPage(body=body,code=code,message=message,title=title)
    res_code = res[0]
    res_message = res[1]
    assert res_code == code
    assert res_message == message


@allure.feature("功能点:对/api/gcp-rm/rmMessage/queryCount接口进行全量测试")
@allure.title("{title}")
@allure.severity(allure.severity_level.BLOCKER)
@pytest.mark.parametrize("body,code,message,title",ReadJsonData(file="rmMessage\\queryCount.json").getBody())
def test_QueryCount(get_session,body,code,message,title):
    res = rmMessage(s=get_session).queryCount(body=body,code=code,message=message,title=title)
    res_code = res[0]
    res_message = res[1]
    assert res_code == code
    assert res_message == message


@allure.feature("功能点:对/api/gcp-rm/rmMessage/read接口进行全量测试")
@allure.title("{title}")
@allure.severity(allure.severity_level.BLOCKER)
@pytest.mark.parametrize("body,code,message,title",ReadJsonData(file="rmMessage\\read.json").getBody())
def test_Read(get_session,body,code,message,title):
    res = rmMessage(s=get_session).read(body=body,code=code,message=message,title=title)
    res_code = res[0]
    res_message = res[1]
    assert res_code == code
    assert res_message == message


@allure.feature("功能点:对/api/gcp-rm/rmMessage/readAll接口进行全量测试")
@allure.title("{title}")
@allure.severity(allure.severity_level.BLOCKER)
@pytest.mark.parametrize("body,code,message,title",ReadJsonData(file="rmMessage\\readAll.json").getBody())
def test_ReadAll(get_session,body,code,message,title):
    res = rmMessage(s=get_session).readAll(body=body,code=code,message=message,title=title)
    res_code = list(res)[0]
    res_message = list(res)[1]
    assert res_code == code
    assert res_message == message


