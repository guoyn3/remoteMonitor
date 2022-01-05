'''
def pytest_collection_modifyitems(items):
    """
    测试用例收集完成时，将收集到的item的name和nodeid的中文显示在控制台上
    :return:
    """
    for item in items:
        item.name = item.name.encode('utf-8').decode("unicode_escape")
        item_nodeid = item.nodeid.encode('utf-8').decode("unicode_escape")
'''
import base
import pytest
import requests
import time
from common.connectMysql import ConnectMysql
from rm.api.rmMonitorApply import rmMonitorApply
from rm.api.rmSubject import rmSubject
from rm.api.rmApprovalRecord import rmApprovalRecord
import sys


# 告诉pytest运行前先检索当前路径
#sys.path.append('E:\\workspace\\python\\GCP')
conn = ConnectMysql()


@pytest.fixture(scope='session')
def get_session():
    s = requests.session()
    res = s.post(url="http://10.0.6.78/gateway/login",
                 json={"username": "gtest1", "password": "123456"},
                 headers={"content-type": "application/json;charset=UTF-8"})
    token = res.json()["data"]["token"]
    yield s
    requests.post(url="http://10.0.6.78/gateway/logout",
                  headers={"Authorization":token})


@pytest.fixture(scope="function")
def del_rmApprovalId():
    rmApprovalId = conn.selectSql(
        sql="select id from rm_approval  where `create_id` = '1462974935490670593' and `type` = 'PROJECT_MONITOR' and operation = '测试新增审批表' order by create_time desc",
        size=1)
    print(rmApprovalId[0]["id"])
    return rmApprovalId[0]["id"]


@pytest.fixture(scope="function")
def get_projectId(get_session):
    import random
    from rm.api.rmProjectUser import rmProjectUser
    sql = "INSERT INTO `gcp_rm`.`mid_project`(`id`, `project_no`, `project_name`, `spons_name`, `cro_spons_name`, `main_researcher_name`, `trial_phase`, `trial_method`, `test_object_name`, `indications`, `belong_specialty`, `trial_create_time`, `trial_start_date`, `trial_end_time`, `check_name`, `tenant_code`, `create_date_time`, `create_user_id`, `update_date_time`, `update_user_id`, `project_status`, `check_time`) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    data = (
        random.randint(1, 100), f'数据对接{time.strftime("%Y%m%d_%H%M%S")}', f'数据对接{time.strftime("%Y%m%d_%H%M%S")}', '11', '22', '33', '44',
        '55', '66', '77', '88', "2021-12-01 00:00:00", "2021-12-01 00:00:00", None, None, None, None, None, None, None,
        1, None)
    conn.insertSql(sql=sql, data=data)
    get_session.post(url="http://10.0.6.78/api/gcp-rm/syncData/process",
                     headers={"Content-Type": "application/json;charset=UTF-8"})
    id = conn.selectSql(
        sql="select id from rm_project where project_status=2 order by `id` desc limit 0,1")
    rmProjectUser(s=get_session).batchCreate(projectId=id[0]["id"],
                                             userIdList=["1466649494303584258", "1466649354205442049"])
    print(id[0]["id"])
    return id[0]["id"]


@pytest.fixture(scope="function")
def get_rmApprovalId(get_session):
    time.sleep(3)
    get_session.post(url="http://10.0.6.78/api/gcp-rm/sysRmConfig/update",
                     json={"configType": "ADMIN_SP", "id": 2},
                     headers={"content-type": "application/json;charset=UTF-8"})
    rmMonitorApply(s=get_session).create()
    res = get_session.post(url='http://10.0.6.78/api/gcp-rm/rmMonitorApply/findByPage',
                           json={"projectNo": "测试项目0001", "applyStatus": [1, 7], "pageNumber": 1, "pageSize": 10},
                           headers={"content-type": "application/json;charset=UTF-8"})
    rmApprovalId = res.json()["data"]["list"][0]["id"]
    print(rmApprovalId)
    return rmApprovalId


@pytest.fixture(scope="function")
def get_subjectId(get_session):
    time.sleep(3)
    get_session.post(url="http://10.0.6.78/api/gcp-rm/sysRmConfig/update",
                     json={"configType": "ADMIN_SP", "id": 2},
                     headers={"content-type": "application/json;charset=UTF-8"})
    rmSubject(s=get_session).create(subject_no=time.strftime("%Y%m%d%H%M%S"))
    res = get_session.post(url='http://10.0.6.78/api/gcp-rm/rmSubject/findSubjectSnapshotPage',
                           json={"pageSize": 10, "pageNumber": 1, "projectNo": "测试项目0001", "applyStatus": 1,"applyName":"gtest1"},
                           headers={"content-type": "application/json;charset=UTF-8"})
    subjectId = res.json()["data"]["list"][0]["id"]
    print(subjectId)
    return subjectId


@pytest.fixture(scope="function")
def del_projectId(get_session):
    time.sleep(3)
    get_session.post(url="http://10.0.6.78/api/gcp-rm/sysRmConfig/update",
                     json={"configType": "ADMIN_SP", "id": 2},
                     headers={"content-type": "application/json;charset=UTF-8"})
    rmSubject(s=get_session).create()
    res = get_session.post(url='http://10.0.6.78/api/gcp-rm/rmSubject/findSubjectSnapshotPage',
                           json={"pageSize": 10, "pageNumber": 1, "projectNo": "测试项目0001", "applyStatus": 1},
                           headers={"content-type": "application/json;charset=UTF-8"})
    projectId = res.json()["data"]["list"][0]["id"]
    return projectId


@pytest.fixture(scope="function")
def get_rmApprovalRecordId(get_session):
    id = conn.selectSql(
        sql="SELECT id FROM `gcp_rm`.`rm_approval_record` WHERE `authority_desc` = 'rmApprovalRecord_create' LIMIT 0,1",
        size=1)
    print(id[0]["id"])
    return id[0]["id"]


@pytest.fixture(scope="function")
def get_subjectSnapshotDetailId(get_session):
    subject_id = conn.selectSql(sql="SELECT subject_id FROM `gcp_rm`.`rm_snapshot_subject` LIMIT 0,1000",
                                size=1)
    print(subject_id[0]["subject_id"])
    return subject_id[0]["subject_id"]


@pytest.fixture(scope="function")
def get_subjectInfo(get_session):
    info = get_session.post(url="http://10.0.6.78/api/gcp-rm/rmSubject/findByPage",
                            json={"pageSize": 10,
                                  "pageNumber": 1,
                                  "applyStatus": 4,
                                  "projectId": 242},
                            headers={"content-type": "application/json;charset=UTF-8"})
    print(info.json()["data"]["list"][0]["projectId"], info.json()["data"]["list"][0]["id"],
          info.json()["data"]["list"][0]["subjectNo"])
    return info.json()["data"]["list"][0]["projectId"], info.json()["data"]["list"][0]["id"], \
           info.json()["data"]["list"][0]["subjectNo"]
