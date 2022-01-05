import requests
from common.readIni import ReadIni
from common.readJsonData import ReadJsonData


class rmLoginStatistics():
    def __init__(self, s=requests.session()):
        self.s = s
        self.host = ReadIni().getValue(section='host', option='host')

    def create(self, body='', code='', message='', title=''):
        url = self.host + '/api/gcp-rm/rmLoginStatistics/create'
        headers = {"content-type": "application/json;charset=UTF-8"}
        json = body
        res = self.s.post(url=url, headers=headers, json=json)
        return res.json()['code'], res.json()['message']

    def findByPage(self, body='', code='', message='', title=''):
        url = self.host + '/api/gcp-rm/rmLoginStatistics/findByPage'
        headers = {"content-type": "application/json;charset=UTF-8"}
        json = body
        res = self.s.post(url=url, headers=headers, json=json)
        return res.json()['code'], res.json()['message']

    def update(self, body='', code='', message='', title=''):
        url = self.host + '/api/gcp-rm/rmLoginStatistics/update'
        headers = {"content-type": "application/json;charset=UTF-8"}
        json = body
        res = self.s.post(url=url, headers=headers, json=json)
        return res.json()['code'], res.json()['message']


if __name__ == "__main__":
    pass
