import pytest
import allure
from common.readJsonData import ReadJsonData
from rm.api.rmProject import rmProject


@allure.feature("功能点:对/api/gcp-rm/rmProject/bannerMorCount接口进行测试")
@allure.title("查询远程监查总次数成功")
@allure.severity(allure.severity_level.NORMAL)
def test_bannerMorCount(get_session):
    res = rmProject(s=get_session).bannerMorCount()
    res_code = res[0]
    assert res_code == "0"


@allure.feature("功能点:对/api/gcp-rm/rmProject/bannerMorDate接口进行测试")
@allure.title("查询累计监查时间成功")
@allure.severity(allure.severity_level.NORMAL)
def test_bannerMorDate(get_session):
    res = rmProject(s=get_session).bannerMorDate()
    res_code = res[0]
    assert res_code == "0"


@allure.feature("功能点:对/api/gcp-rm/rmProject/bannerSaeReport接口进行测试")
@allure.title("查询SAE上报成功")
@allure.severity(allure.severity_level.NORMAL)
def test_bannerSaeReport(get_session):
    res = rmProject(s=get_session).bannerSaeReport()
    res_code = res[0]
    assert res_code == "0"


@allure.feature("功能点:对/api/gcp-rm/rmProject/projectNumber接口进行测试")
@allure.title("查询累计监查时间成功")
@allure.severity(allure.severity_level.NORMAL)
def test_projectNumber(get_session):
    res = rmProject(s=get_session).projectNumber()
    res_code = res[0]
    assert res_code == "0"


@allure.feature("功能点:对/api/gcp-rm/rmProject/create接口进行全量测试")
@allure.title("界面添加项目")
@allure.severity(allure.severity_level.BLOCKER)
def test_create(get_session):
    res = rmProject(s=get_session).create()
    res_code = res[0]
    res_message = res[1]
    assert res_code == "0"
    assert res_message == "成功!"


@allure.feature("功能点:对/api/gcp-rm/rmProject/update接口进行全量测试")
@allure.title("{title}")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize("body,code,message,title", ReadJsonData(file="rmProject\\update.json").getBody())
def test_update(get_session,body, code, message, title):
    res = rmProject(s=get_session).update(body=body, code=code, message=message, title=title)
    res_code = res[0]
    res_message = res[1]
    assert res_code == str(code)
    assert res_message == message


@allure.feature("功能点:对/api/gcp-rm/rmProject/findById接口进行全量测试")
@allure.title("{title}")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize("body,code,message,title", ReadJsonData(file="rmProject\\findById.json").getBody())
def test_findById(get_session,body, code, message, title):
    res = rmProject(s=get_session).findById(body=body, code=code, message=message, title=title)
    res_code = res[0]
    res_message = res[1]
    assert res_code == str(code)
    assert res_message == message


@allure.feature("功能点:对/api/gcp-rm/rmProject/findByPage接口进行全量测试")
@allure.title("{title}")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize("body,code,message,title", ReadJsonData(file="rmProject\\findByPage.json").getBody())
def test_findByPage(get_session,body, code, message, title):
    res = rmProject(s=get_session).findByPage(body=body, code=code, message=message, title=title)
    res_code = res[0]
    res_message = res[1]
    assert res_code == str(code)
    assert res_message == message


@allure.feature("功能点:对/api/gcp-rm/rmProject/findDetailNum接口进行全量测试")
@allure.title("{title}")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize("body,code,message,title", ReadJsonData(file="rmProject\\findDetailNum.json").getBody())
def test_findDetailNum(get_session,body, code, message, title):
    res = rmProject(s=get_session).findDetailNum(body=body, code=code, message=message, title=title)
    res_code = res[0]
    res_message = res[1]
    assert res_code == str(code)
    assert res_message == message

