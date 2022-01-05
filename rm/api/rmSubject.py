import requests
from common.readIni import ReadIni
from common.readJsonData import ReadJsonData
import time
import random


class rmSubject():
    def __init__(self, s=requests.session()):
        self.s = s
        self.host = ReadIni().getValue(section='host', option='host')

    def create(self, subject_no=time.strftime("%Y%m%d%H%M%S") ,icfDate=time.strftime("%Y-%m-%d")):
        url = self.host + '/api/gcp-rm/rmSubject/create'
        headers = {"content-type": "application/json;charset=UTF-8"}
        json = {
            "phoneticShort": "test",
            "subjectNo": f"受试者{subject_no}",
            "icfDate": icfDate,
            "screenDate": "",
            "dropDate": "",
            "inclusionNo": "",
            "dropReason": "",
            "inpatientSn": "1",
            "projectId": 242
        }
        res = self.s.post(url=url, headers=headers, json=json)
        return res.json()['code'], res.json()['message']

    def findById(self, body='', code='', message='', title=''):
        url = self.host + '/api/gcp-rm/rmSubject/findById'
        headers = {"content-type": "application/json;charset=UTF-8"}
        json = body
        res = self.s.post(url=url, headers=headers, json=json)
        return res.json()['code'], res.json()['message']

    def findByPage(self, body='', code='', message='', title=''):
        url = self.host + '/api/gcp-rm/rmSubject/findByPage'
        headers = {"content-type": "application/json;charset=UTF-8"}
        json = body
        res = self.s.post(url=url, headers=headers, json=json)
        return res.json()['code'], res.json()['message']

    def update(self,projectId="242",id="1754",subjectNo="2021-12-16_910"):
        url = self.host + '/api/gcp-rm/rmSubject/update'
        headers = {"content-type": "application/json;charset=UTF-8"}
        json = {
            "phoneticShort":"test",
            "subjectNo":subjectNo,
            "icfDate":"2021-12-16",
            "screenDate":None,
            "dropDate":"",
            "inclusionNo":"",
            "dropReason":"",
            "id":id,
            "inpatientSn":"1",
            "projectId":projectId
        }
        res = self.s.post(url=url, headers=headers, json=json)
        return res.json()['code'], res.json()['message']

    def checkUnique(self, body='', code='', message='', title=''):
        url = self.host + '/api/gcp-rm/rmSubject/checkUnique'
        headers = {"content-type": "application/json;charset=UTF-8"}
        json = body
        res = self.s.post(url=url, headers=headers, json=json)
        return res.json()['code'], res.json()['message']

    def cancelById(self, id=''):
        url = self.host + '/api/gcp-rm/rmSubject/cancelById'
        headers = {"content-type": "application/json;charset=UTF-8"}
        json = {
            "id": id
        }
        res = self.s.post(url=url, headers=headers, json=json)
        return res.json()['code'], res.json()['message']

    def subjectNumber(self):
        url = self.host + '/api/gcp-rm/rmSubject/subjectNumber'
        headers = {"content-type": "application/json;charset=UTF-8"}
        res = self.s.post(url=url, headers=headers)
        return res.json()['code'], res.json()['message']

    def viewSubject360(self,
                       cdrUrl='http://10.0.6.78/new_cdr_ui/#/PatientDetailPage/undefined/undefined?sdvJson={"upload_show":true,"tab_list":["diagnose","medical_record_home_page_new","medical_document","drug","inspection","imaging_exam","operation","nursing_record","nursing","measuring_record","non_drug_orders","forsz","micm","img_file"],"inpatientSn":"0001"}'):
        url = self.host + '/api/gcp-rm/rmSubject/viewSubject360'
        headers = {"content-type": "application/json;charset=UTF-8"}
        body = {
            "cdrUrl": cdrUrl
        }
        res = self.s.get(url=url, headers=headers, )
        res = self.s.post(url=url, headers=headers, params=body)
        if res.json()["code"] == "0":
            print("查看受试者360成功")
        else:
            print("查看受试者360失败")
        return res.json()['code'], res.json()['message']

    def findSubjectSnapshotPage(self, body='', code='', message='', title=''):
        url = self.host + '/api/gcp-rm/rmSubject/findSubjectSnapshotPage'
        headers = {"content-type": "application/json;charset=UTF-8"}
        json = body
        res = self.s.post(url=url, headers=headers, json=json)
        return res.json()['code'], res.json()['message']

    def subjectSnapshotDetail(self, id=''):
        url = self.host + '/api/gcp-rm/rmSubject/subjectSnapshotDetail'
        headers = {"content-type": "application/json;charset=UTF-8"}
        json = {
            "id": id
        }
        res = self.s.post(url=url, headers=headers, json=json)
        return res.json()['code'], res.json()['message']


if __name__ == "__main__":
    from rm.api.gateway import gateway
    lg = gateway().login()
    data = ReadJsonData(file="rmSubject\\subjectSnapshotDetail.json").getBody()
    a = rmSubject(s=lg[2]).viewSubject360()
    # t = rmSubject(s=lg[2]).subjectSnapshotDetail(body=data[0][0],code=data[0][1],message=data[0][2],title=data[0][3])
