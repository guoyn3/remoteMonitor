import requests
from common.readIni import ReadIni
from common.readJsonData import ReadJsonData


class rmUser():
    def __init__(self, s=requests.session()):
        self.s = s
        self.host = ReadIni().getValue(section="host", option='host')

    def createOrUpdate(self, body='', code='', message='', title=''):
        url = self.host + '/api/gcp-rm/rmUser/createOrUpdate'
        headers = {"content-type": "application/json;charset=UTF-8"}
        json = body
        res = self.s.post(url=url, headers=headers, json=json)
        return res.json()['code'], res.json()['message']

    def findById(self, body='', code='', message='', title=''):
        url = self.host + '/api/gcp-rm/rmUser/findById'
        headers = {"content-type": "application/json;charset=UTF-8"}
        json = body
        res = self.s.post(url=url, headers=headers, json=json)
        return res.json()['code'], res.json()['message']

    def findByPage(self, body='', code='', message='', title=''):
        url = self.host + '/api/gcp-user/sysUser/findByPage'
        headers = {"content-type": "application/json;charset=UTF-8"}
        json = body
        res = self.s.post(url=url, headers=headers, json=json)
        return res.json()['code'], res.json()['message']

    def findUser(self, body='', code='', message='', title=''):
        url = self.host + '/api/gcp-rm/rmUser/findUser'
        headers = {"content-type": "application/json;charset=UTF-8"}
        json = body
        res = self.s.post(url=url, headers=headers, json=json)
        return res.json()['code'], res.json()['message']


if __name__ == "__main__":
    pass
