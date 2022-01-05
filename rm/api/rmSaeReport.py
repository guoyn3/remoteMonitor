import requests
from common.readIni import ReadIni
from common.readJsonData import ReadJsonData

class rmSaeReport():
    def __init__(self,s=requests.session()):
        self.s=s
        self.host = ReadIni().getValue(section='host', option='host')

    def create(self,body='',code='',message='',title=''):
        url = self.host + '/api/gcp-rm/rmSaeReport/create'
        headers = {"content-type": "application/json;charset=UTF-8"}
        json = body
        res = self.s.post(url=url, headers=headers, json=json)
        return res.json()['code'], res.json()['message']

    def deleteById(self,body='',code='',message='',title=''):
        url = self.host + '/api/gcp-rm/rmSaeReport/deleteById'
        headers = {"content-type": "application/json;charset=UTF-8"}
        json = body
        res = self.s.post(url=url, headers=headers, json=json)
        return res.json()['code'], res.json()['message']

    def findById(self,body='',code='',message='',title=''):
        url = self.host + '/api/gcp-rm/rmSaeReport/findById'
        headers = {"content-type": "application/json;charset=UTF-8"}
        json = body
        res = self.s.post(url=url, headers=headers, json=json)
        return res.json()['code'], res.json()['message']

    def findByPage(self,body='',code='',message='',title=''):
        url = self.host + '/api/gcp-rm/rmSaeReport/findByPage'
        headers = {"content-type": "application/json;charset=UTF-8"}
        json = body
        res = self.s.post(url=url, headers=headers, json=json)
        return res.json()['code'], res.json()['message']

    def update(self,body='',code='',message='',title=''):
        url = self.host + '/api/gcp-rm/rmSaeReport/update'
        headers = {"content-type": "application/json;charset=UTF-8"}
        json = body
        res = self.s.post(url=url, headers=headers, json=json)
        return res.json()['code'], res.json()['message']

if __name__ =="__main__":
    from rm.api.gateway import gateway
    lg = gateway().login()
    data = ReadJsonData(file="rmSaeReport\\findById.json").getBody()
    fbi = rmSaeReport(s=lg[2]).findById(body=data[0][0],code=data[0][1],message=data[0][2],title=data[0][3])