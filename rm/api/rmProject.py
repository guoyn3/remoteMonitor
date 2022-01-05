import requests
from common.readIni import ReadIni
from common.readJsonData import ReadJsonData
import time


class rmProject:
    def __init__(self, s=requests.session()):
        self.s = s
        self.host = ReadIni().getValue(section='host', option='host')

    def bannerMorCount(self):
        url = self.host + "/api/gcp-rm/rmProject/bannerMorCount"
        headers = {"Content-Type": "application/json; charset=UTF-8"}
        res = self.s.post(url=url, headers=headers)
        return res.json()['code'], res.json()['message']

    def bannerMorDate(self):
        url = self.host + "/api/gcp-rm/rmProject/bannerMorDate"
        headers = {"Content-Type": "application/json; charset=UTF-8"}
        res = self.s.post(url=url, headers=headers)
        return res.json()['code'], res.json()['message']

    def bannerSaeReport(self):
        url = self.host + "/api/gcp-rm/rmProject/bannerSaeReport"
        headers = {"Content-Type": "application/json; charset=UTF-8"}
        res = self.s.post(url=url, headers=headers)
        return res.json()['code'], res.json()['message']

    def projectNumber(self):
        url = self.host + '/api/gcp-rm/rmProject/projectNumber'
        headers = {"content-type": "application/json;charset=UTF-8"}
        res = self.s.post(url=url, headers=headers)
        return res.json()['code'], res.json()['message']

    def create(self, projectNo=time.strftime("%Y%m%d_%H%M%S")):
        url = self.host + '/api/gcp-rm/rmProject/create'
        headers = {"content-type": "application/json;charset=UTF-8"}
        json = {
            "belongSpecialty": "所属专业",
            "croSponsName": "CRO",
            "indications": "适应症",
            "mainResearcherName": "主要研究者",
            "projectName": "guo测试项目",
            "projectNo": f"界面添加{projectNo}",
            "sponsName": "申办方",
            "testObjectName": "受试品名称",
            "trialCreateTime": "2021-12-01 00:00:00",
            "trialEndTime": "",
            "trialMethod": "试验方法",
            "trialPhase": "实验分期",
            "trialStartDate": "2021-12-01 00:00:00",
            "userIds": ["1462974935490670593", "1463026627703779329", "1466649354205442049", "1466649494303584258"]
        }
        res = self.s.post(url=url, headers=headers, json=json)
        return res.json()['code'], res.json()['message']

    def deleteById(self, body='', code='', message='', title=''):
        url = self.host + '/api/gcp-rm/rmProject/deleteById'
        headers = {"content-type": "application/json;charset=UTF-8"}
        json = body
        res = self.s.post(url=url, headers=headers, json=json)
        return res.json()['code'], res.json()['message']

    def update(self, body='', code='', message='', title=''):
        url = self.host + '/api/gcp-rm/rmProject/update'
        headers = {"content-type": "application/json;charset=UTF-8"}
        json = body
        res = self.s.post(url=url, headers=headers, json=json)
        return res.json()['code'], res.json()['message']

    def findById(self, body='', code='', message='', title=''):
        url = self.host + '/api/gcp-rm/rmProject/findById'
        headers = {"content-type": "application/json;charset=UTF-8"}
        json = body
        res = self.s.post(url=url, headers=headers, json=json)
        return res.json()['code'], res.json()['message']

    def findByPage(self, body='', code='', message='', title=''):
        url = self.host + '/api/gcp-rm/rmProject/findByPage'
        headers = {"content-type": "application/json;charset=UTF-8"}
        json = body
        res = self.s.post(url=url, headers=headers, json=json)
        return res.json()['code'], res.json()['message']

    def findDetailNum(self, body='', code='', message='', title=''):
        url = self.host + '/api/gcp-rm/rmProject/findDetailNum'
        headers = {"content-type": "application/json;charset=UTF-8"}
        json = body
        res = self.s.post(url=url, headers=headers, json=json)
        return res.json()['code'], res.json()['message']


if __name__ == "__main__":
    from rm.api.gateway import gateway
    lg = gateway().login()
    from common.readJsonData import ReadJsonData
    bmc = rmProject(s=list(lg)[2]).bannerMorCount()
    # bmd = rmProject(s=list(lg)[2]).bannerMorDate()
    b6 = ReadJsonData(file='rmProject\\findDetailNum.json').getBody()
    # rmProject(s=list(lg)[2]).findDetailNum(body=list(b6)[0][0],code=list(b6)[0][1],message=list(b6)[0][2],title=list(b6)[0][3])
