import pytest
import allure
from rm.api.rmSubject import rmSubject
from common.readJsonData import ReadJsonData


@allure.feature("功能点:对/api/gcp-rm/rmSubject/create接口进行测试")
@allure.title("添加受试者成功")
@allure.severity(allure.severity_level.NORMAL)
def test_create(get_session):
    res = rmSubject(s=get_session).create()
    res_code = res[0]
    res_message = res[1]
    assert res_code == "0"
    assert res_message == "成功!"


@allure.feature("功能点:对/api/gcp-rm/rmSubject/findById接口进行测试")
@allure.title("{title}")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize("body,code,message,title", ReadJsonData(file="rmSubject\\findById.json").getBody())
def test_findById(get_session, body, code, message, title):
    res = rmSubject(s=get_session).findById(body=body, code=code, message=message, title=title)
    res_code = res[0]
    res_message = res[1]
    assert res_code == str(code)
    assert res_message == message


@allure.feature("功能点:对/api/gcp-rm/rmSubject/findByPage接口进行测试")
@allure.title("{title}")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize("body,code,message,title", ReadJsonData(file="rmSubject\\findByPage.json").getBody())
def test_findByPage(get_session, body, code, message, title):
    res = rmSubject(s=get_session).findByPage(body=body, code=code, message=message, title=title)
    res_code = res[0]
    res_message = res[1]
    assert res_code == str(code)
    assert res_message == message


@allure.feature("功能点:对/api/gcp-rm/rmSubject/update接口进行测试")
@allure.title("编辑受试者")
@allure.severity(allure.severity_level.NORMAL)
def test_update(get_session, get_subjectInfo):
    res = rmSubject(s=get_session).update(projectId=get_subjectInfo[0],id=get_subjectInfo[1],subjectNo=get_subjectInfo[2])
    res_code = res[0]
    res_message = res[1]
    assert res_code == "0"
    assert res_message == "成功!"


@allure.feature("功能点:对/api/gcp-rm/rmSubject/checkUnique接口进行测试")
@allure.title("{title}")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize("body,code,message,title", ReadJsonData(file="rmSubject\\checkUnique.json").getBody())
def test_checkUnique(get_session, body, code, message, title):
    res = rmSubject(s=get_session).checkUnique(body=body, code=code, message=message, title=title)
    res_code = res[0]
    res_message = res[1]
    assert res_code == str(code)
    assert res_message == message


@allure.feature("功能点:对/api/gcp-rm/rmSubject/cancelById接口进行测试")
@allure.title("撤销受试者")
@allure.severity(allure.severity_level.NORMAL)
def test_cancelById(get_session,get_subjectId):
    res = rmSubject(s=get_session).cancelById(id=get_subjectId)
    res_code = res[0]
    res_message = res[1]
    assert res_code == "0"
    assert res_message == "成功!"


@allure.feature("功能点:对/api/gcp-rm/rmSubject/subjectNumber接口进行测试")
@allure.title("查询受试者个数成功")
@allure.severity(allure.severity_level.NORMAL)
def test_subjectNumber(get_session):
    res = rmSubject(s=get_session).subjectNumber()
    res_code = res[0]
    assert res_code == "0"


'''@allure.feature("功能点:对/api/gcp-rm/rmSubject/viewSubject360接口进行测试")
@allure.title("{title}")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize("body,code,message,title", ReadJsonData(file="rmSubject\\viewSubject360.json").getBody())
def test_viewSubject360(get_session, body, code, message, title):
    res = rmSubject(s=get_session).viewSubject360(body=body, code=code, message=message, title=title)
    res_code = res[0]
    res_message = res[1]
    assert res_code == str(code)
    assert res_message == message'''


@allure.feature("功能点:对/api/gcp-rm/rmSubject/findSubjectSnapshotPage接口进行测试")
@allure.title("{title}")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize("body,code,message,title",
                         ReadJsonData(file="rmSubject\\findSubjectSnapshotPage.json").getBody())
def test_findSubjectSnapshotPage(get_session, body, code, message, title):
    res = rmSubject(s=get_session).findSubjectSnapshotPage(body=body, code=code, message=message, title=title)
    res_code = res[0]
    res_message = res[1]
    assert res_code == str(code)
    assert res_message == message


@allure.feature("功能点:对/api/gcp-rm/rmSubject/subjectSnapshotDetail接口进行测试")
@allure.title("获取受试者快照详情")
@allure.severity(allure.severity_level.NORMAL)
def test_subjectSnapshotDetail(get_session, get_subjectSnapshotDetailId):
    res = rmSubject(s=get_session).subjectSnapshotDetail(id=get_subjectSnapshotDetailId)
    res_code = res[0]
    res_message = res[1]
    assert res_code == "0"
    assert res_message == "成功!"
