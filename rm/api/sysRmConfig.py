import requests
from common.readIni import ReadIni
from common.readJsonData import ReadJsonData


class sysRmConfig():
    def __init__(self, s=requests.session()):
        self.s = s
        self.host = ReadIni().getValue(section='host', option='host')

    def update(self, body='', code='', message='', title=''):
        url = self.host + '/api/gcp-rm/sysRmConfig/update'
        headers = {"Content-Type": "application/json;charset=UTF-8"}
        json = body
        res = self.s.post(url=url, headers=headers, json=json)
        return res.json()['code'], res.json()['message']

    def findProjectMonitor(self):
        url = self.host + '/api/gcp-rm/sysRmConfig/findProjectMonitor'
        headers = {"Content-Type": "application/json;charset=UTF-8"}
        res = self.s.post(url=url, headers=headers)
        return res.json()['code'], res.json()['message']

    def findSubjectMonitor(self):
        url = self.host + '/api/gcp-rm/sysRmConfig/findSubjectMonitor'
        headers = {"Content-Type": "application/json;charset=UTF-8"}
        res = self.s.post(url=url, headers=headers)
        return res.json()['code'], res.json()['message']


if __name__ == "__main__":
    pass
