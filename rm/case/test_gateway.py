import pytest
import allure
from rm.api.gateway import gateway
from common.readJsonData import ReadJsonData


@allure.feature("功能点:对/gateway/login接口进行全量测试")
@allure.title("登录-{title}")
@allure.severity(allure.severity_level.BLOCKER)
@pytest.mark.parametrize("body, code, message, title", ReadJsonData(file="gateway\\login.json").getBody())
# @pytest.mark.parametrize("body,code,message",ReadJsonData(file="gateway_login.json").getBody(),ids["登录成功","登录失败","登录失败"])
def test_Login(body, code, message, title):
    res = gateway().login(body=body, code=code, message=message, title=title)
    res_code = res[0]
    res_message = res[1]
    assert res_code == code
    assert res_message == message
