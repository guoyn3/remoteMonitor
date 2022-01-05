import pytest
import allure
from rm.api.rmLoginStatistics import rmLoginStatistics
from common.readJsonData import ReadJsonData


@allure.feature("功能点：对/api/gcp-rm/rmLoginStatistics/findByPage接口进行测试")
@allure.title("{title}")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize("body,code,message,title",ReadJsonData(file="rmLoginStatistics\\findByPage.json").getBody())
def test_findByPage(get_session, body, code, message, title):
    res = rmLoginStatistics(s=get_session).findByPage(body=body, code=code, message=message, title=title)
    res_code = res[0]
    res_message = res[1]
    assert res_code == str(code)
    assert res_message == message
