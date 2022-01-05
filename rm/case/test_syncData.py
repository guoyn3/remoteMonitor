import pytest
import allure
from rm.api.syncData import syncData


@allure.feature("功能点：对/api/gcp-rm/syncData/process接口进行测试")
@allure.title("处理数据同步成功")
@allure.severity(allure.severity_level.NORMAL)
def test_syncData(get_session):
    res = syncData(s=get_session).process()
    res_code = res[0]
    assert res_code == "0"
