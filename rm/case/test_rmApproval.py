import pytest
import allure
from rm.api.rmApproval import rmApproval
from common.readJsonData import ReadJsonData


@allure.feature("功能点:对/api/gcp-rm/rmApproval/create接口进行测试")
@allure.title("{title}")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize("body,code,message,title", ReadJsonData(file="rmApproval\\create.json").getBody())
def test_create(get_session, body, code, message, title):
    res = rmApproval(s=get_session).create(body=body, code=code, message=message, title=title)
    res_code = res[0]
    res_message = res[1]
    assert res_code == str(code)
    assert res_message == message


@allure.feature("功能点:对/api/gcp-rm/rmApproval/deleteById接口进行测试")
@allure.title("删除审批表")
@allure.severity(allure.severity_level.NORMAL)
def test_deleteById(get_session, del_rmApprovalId):
    res = rmApproval(s=get_session).deleteById(id=del_rmApprovalId)
    res_code = res[0]
    res_message = res[1]
    assert res_code == "0"
    assert res_message == "成功!"


@allure.feature("功能点:对/api/gcp-rm/rmApproval/findByPage接口进行测试")
@allure.title("{title}")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize("body,code,message,title", ReadJsonData(file="rmApproval\\findByPage.json").getBody())
def test_findByPage(get_session, body, code, message, title):
    res = rmApproval(s=get_session).findByPage(body=body, code=code, message=message, title=title)
    res_code = res[0]
    res_message = res[1]
    assert res_code == str(code)
    assert res_message == message


@allure.feature("功能点:对/api/gcp-rm/rmApproval/monitorApplyNumber接口进行测试")
@allure.title("获取远程监查次数成功")
@allure.severity(allure.severity_level.NORMAL)
def test_monitorApplyNumber(get_session):
    res = rmApproval(s=get_session).monitorApplyNumber()
    res_code = res[0]
    assert res_code == "0"


@allure.feature("功能点:对/api/gcp-rm/rmApproval/monitorPass接口进行测试")
@allure.title("远程监查审批通过")
@allure.severity(allure.severity_level.NORMAL)
def test_monitorPass(get_session,get_rmApprovalId):
    print("审批通过的远程监查id为："+get_rmApprovalId)
    res = rmApproval(s=get_session).monitorPass(id=get_rmApprovalId)
    res_code = res[0]
    res_message = res[1]
    assert res_code == "0"
    assert res_message == "成功!"


@allure.feature("功能点:对/api/gcp-rm/rmApproval/monitorRefuse接口进行测试")
@allure.title("远程监查审批不通过")
@allure.severity(allure.severity_level.NORMAL)
def test_monitorRefuse(get_session,get_rmApprovalId):
    print("审批不通过的远程监查id为："+get_rmApprovalId)
    res = rmApproval(s=get_session).monitorRefuse(id=get_rmApprovalId)
    res_code = res[0]
    res_message = res[1]
    assert res_code == "0"
    assert res_message == "成功!"


@allure.feature("功能点:对/api/gcp-rm/rmApproval/process接口进行测试")
@allure.title("{title}")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize("body,code,message,title", ReadJsonData(file="rmApproval\\process.json").getBody())
def test_process(get_session, body, code, message, title):
    res = rmApproval(s=get_session).process(body=body, code=code, message=message, title=title)
    res_code = res[0]
    res_message = res[1]
    assert res_code == str(code)
    assert res_message == message


@allure.feature("功能点:对/api/gcp-rm/rmApproval/projectPass接口进行测试")
@allure.title("审批项目通过")
@allure.severity(allure.severity_level.NORMAL)
def test_projectPass(get_session,get_projectId):
    res = rmApproval(s=get_session).projectPass(id=get_projectId)
    res_code = res[0]
    res_message = res[1]
    assert res_code == "0"
    assert res_message == "成功!"


@allure.feature("功能点:对/api/gcp-rm/rmApproval/startProjectNumber接口进行测试")
@allure.title("获取累计启动项目数")
@allure.severity(allure.severity_level.NORMAL)
def test_startProjectNumber(get_session):
    res = rmApproval(s=get_session).startProjectNumber()
    res_code = res[0]
    assert res_code == "0"


@allure.feature("功能点:对/api/gcp-rm/rmApproval/update接口进行测试")
@allure.title("{title}")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize("body,code,message,title", ReadJsonData(file="rmApproval\\update.json").getBody())
def test_update(get_session, body, code, message, title):
    res = rmApproval(s=get_session).update(body=body, code=code, message=message, title=title)
    res_code = res[0]
    res_message = res[1]
    assert res_code == str(code)
    assert res_message == message


@allure.feature("功能点:对/api/gcp-rm/rmApproval/subjectPass接口进行测试")
@allure.title("受试者审批通过")
@allure.severity(allure.severity_level.NORMAL)
def test_subjectPass(get_session,get_subjectId):
    print("审批通过的受试者id为："+get_subjectId)
    res = rmApproval(s=get_session).subjectPass(id=get_subjectId)
    res_code = res[0]
    res_message = res[1]
    assert res_code == "0"
    assert res_message == "成功!"


@allure.feature("功能点:对/api/gcp-rm/rmApproval/subjectRefuse接口进行测试")
@allure.title("受试者审批不通过")
@allure.severity(allure.severity_level.NORMAL)
def test_subjectRefuse(get_session,get_subjectId):
    print("审批不通过的受试者id为：" + get_subjectId)
    res = rmApproval(s=get_session).subjectRefuse(id=get_subjectId)
    res_code = res[0]
    res_message = res[1]
    assert res_code == "0"
    assert res_message == "成功!"


@allure.feature("功能点:对/api/gcp-rm/rmApproval/subjectCancel接口进行测试")
@allure.title("受试者审批撤销")
@allure.severity(allure.severity_level.NORMAL)
def test_subjectCancel(get_session,get_subjectId):
    print("撤销的受试者id为：" + get_subjectId)
    res = rmApproval(s=get_session).subjectCancel(id=get_subjectId)
    res_code = res[0]
    res_message = res[1]
    assert res_code == "0"
    assert res_message == "成功!"
