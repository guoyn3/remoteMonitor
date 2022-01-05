import requests
from common.readIni import ReadIni
from common.readJsonData import ReadJsonData

class rmApprovalRecord():
    def __init__(self,s=requests.session()):
        self.s=s
        self.host = ReadIni().getValue(section='host', option='host')

    def create(self,body='',code='',message='',title=''):
        url = self.host + '/api/gcp-rm/rmApprovalRecord/create'
        headers = {"content-type": "application/json;charset=UTF-8"}
        json = body
        res = self.s.post(url=url, headers=headers, json=json)
        return res.json()['code'], res.json()['message']

    def deleteById(self,id=''):
        url = self.host + '/api/gcp-rm/rmApprovalRecord/deleteById'
        headers = {"content-type": "application/json;charset=UTF-8"}
        json = {
            "id":id
        }
        res = self.s.post(url=url, headers=headers, json=json)
        return res.json()['code'], res.json()['message']

    def findById(self,body='',code='',message='',title=''):
        url = self.host + '/api/gcp-rm/rmApprovalRecord/findById'
        headers = {"content-type": "application/json;charset=UTF-8"}
        json = body
        res = self.s.post(url=url, headers=headers, json=json)
        return res.json()['code'], res.json()['message']

    def findByPage(self,body='',code='',message='',title=''):
        url = self.host + '/api/gcp-rm/rmApprovalRecord/findByPage'
        headers = {"content-type": "application/json;charset=UTF-8"}
        json = body
        res = self.s.post(url=url, headers=headers, json=json)
        return res.json()['code'], res.json()['message']

    def update(self,body='',code='',message='',title=''):
        url = self.host + '/api/gcp-rm/rmApprovalRecord/update'
        headers = {"content-type": "application/json;charset=UTF-8"}
        json = body
        res = self.s.post(url=url, headers=headers, json=json)
        return res.json()['code'], res.json()['message']

if __name__ =="__main__":
    pass