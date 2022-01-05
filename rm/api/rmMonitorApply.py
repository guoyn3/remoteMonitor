import requests
from common.readIni import ReadIni
from common.readJsonData import ReadJsonData
import time

class rmMonitorApply():
    def __init__(self, s=requests.session()):
        self.s = s
        self.host = ReadIni().getValue(section='host', option='host')

    def create(self, startTime=time.strftime("%Y-%m-%d 00:00:00"),endTime=time.strftime("%Y-%m-%d 23:59:59")):
        url = self.host + '/api/gcp-rm/rmMonitorApply/create'
        headers = {"content-type": "application/json;charset=UTF-8"}
        json = {
            "id": "",
            "projectNo": "测试项目0001",
            "startTime": startTime,
            "endTime": endTime,
            "monitorPtype": 1,
            "monitorTarget": "",
            "subjectType": 2,
            "subjects": "2021-12-14_34",
            "monitorStype": "diagnose",
            "timeType": 1,
            "startNum": 1,
            "validStartTime": ["2021-12-13T16:00:00.000Z", "2021-12-13T16:00:00.000Z"],
            "projectId": "242"
        }
        res = self.s.post(url=url, headers=headers, json=json)
        return res.json()['code'], res.json()['message']

    def deleteById(self, body='', code='', message='', title=''):
        url = self.host + '/api/gcp-rm/rmMonitorApply/deleteById'
        headers = {"content-type": "application/json;charset=UTF-8"}
        json = body
        res = self.s.post(url=url, headers=headers, json=json)
        return res.json()['code'], res.json()['message']

    def findById(self, body='', code='', message='', title=''):
        url = self.host + '/api/gcp-rm/rmMonitorApply/findById'
        headers = {"content-type": "application/json;charset=UTF-8"}
        json = body
        res = self.s.post(url=url, headers=headers, json=json)
        return res.json()['code'], res.json()['message']

    def findByPage(self, body='', code='', message='', title=''):
        url = self.host + '/api/gcp-rm/rmMonitorApply/findByPage'
        headers = {"content-type": "application/json;charset=UTF-8"}
        json = body
        res = self.s.post(url=url, headers=headers, json=json)
        return res.json()['code'], res.json()['message']

    def update(self, body='', code='', message='', title=''):
        url = self.host + '/api/gcp-rm/rmMonitorApply/update'
        headers = {"content-type": "application/json;charset=UTF-8"}
        json = body
        res = self.s.post(url=url, headers=headers, json=json)
        return res.json()['code'], res.json()['message']

    def getMonitorStype(self):
        url = self.host + '/api/gcp-rm/rmMonitorApply/getMonitorStype'
        headers = {"content-type": "application/json;charset=UTF-8"}
        res = self.s.post(url=url, headers=headers)
        return res.json()['code'], res.json()['message']

    def undoneMonitorApply(self, id='', projectId=''):
        url = self.host + '/api/gcp-rm/rmMonitorApply/undoneMonitorApply'
        headers = {"content-type": "application/json;charset=UTF-8"}
        json = {
            "projectId": projectId,
            "id": id
        }
        res = self.s.post(url=url, headers=headers, json=json)
        return res.json()['code'], res.json()['message']

    def canApply(self, body='', code='', message='', title=''):
        url = self.host + '/api/gcp-rm/rmMonitorApply/canApply'
        headers = {"content-type": "application/json;charset=UTF-8"}
        json = body
        res = self.s.post(url=url, headers=headers, json=json)
        return res.json()['code'], res.json()['message']


if __name__ == "__main__":
    # pass
    rmMonitorApply().create()
