import requests
from common.readIni import ReadIni
from common.readJsonData import ReadJsonData


class rmProjectUser:
    def __init__(self, s=requests.session()):
        self.s = s
        self.host = ReadIni().getValue(section='host', option='host')

    def batchCreate(self, projectId="180",userIdList=["1462974935490670593", "1463026627703779329"]):
        url = self.host + '/api/gcp-rm/rmProjectUser/batchCreate'
        headers = {"content-type": "application/json;charset=UTF-8"}
        json = {
            "projectId": projectId,
            "userIdList": userIdList
        }
        res = self.s.post(url=url, headers=headers, json=json)
        return res.json()['code'], res.json()['message']

    def batchDelete(self, body='', code='', message='', title=''):
        url = self.host + '/api/gcp-rm/rmProjectUser/batchDelete'
        headers = {"content-type": "application/json;charset=UTF-8"}
        json = body
        res = self.s.post(url=url, headers=headers, json=json)
        return res.json()['code'], res.json()['message']

    def checkUserProject(self, body='', code='', message='', title=''):
        url = self.host + '/api/gcp-rm/rmProjectUser/checkUserProject'
        headers = {"content-type": "application/json;charset=UTF-8"}
        json = body
        res = self.s.post(url=url, headers=headers, json=json)
        return res.json()['code'], res.json()['message']

    def findUserProjectCount(self, body='', code='', message='', title=''):
        url = self.host + '/api/gcp-rm/rmProjectUser/findUserProjectCount'
        headers = {"content-type": "application/json;charset=UTF-8"}
        json = body
        res = self.s.post(url=url, headers=headers, json=json)
        return res.json()['code'], res.json()['message']

    def findProjectUser(self, body='', code='', message='', title=''):
        url = self.host + '/api/gcp-rm/rmProjectUser/findProjectUser'
        headers = {"content-type": "application/json;charset=UTF-8"}
        json = body
        res = self.s.post(url=url, headers=headers, json=json)
        return res.json()['code'], res.json()['message']


if __name__ == "__main__":
    pass
