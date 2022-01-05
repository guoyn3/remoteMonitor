import requests
from common.readIni import ReadIni
from common.readJsonData import ReadJsonData

class rmProjectSnapshot():
    def __init__(self,s=requests.session()):
        self.s=s
        self.host = ReadIni().getValue(section='host', option='host')

    def findById(self,body='',code='',message='',title=''):
        url = self.host + '/api/gcp-rm/rmProjectSnapshot/findById'
        headers = {"content-type": "application/json;charset=UTF-8"}
        json = body
        res = self.s.post(url=url, headers=headers, json=json)
        return res.json()['code'], res.json()['message']

    def findByPage(self,body='',code='',message='',title=''):
        url = self.host + '/api/gcp-rm/rmProjectSnapshot/findByPage'
        headers = {"content-type": "application/json;charset=UTF-8"}
        json = body
        res = self.s.post(url=url, headers=headers, json=json)
        return res.json()['code'], res.json()['message']

    def findProjectUser(self,body='',code='',message='',title=''):
        url = self.host + '/api/gcp-rm/rmProjectSnapshot/findProjectUser'
        headers = {"content-type": "application/json;charset=UTF-8"}
        json = body
        res = self.s.post(url=url, headers=headers, json=json)
        return res.json()['code'], res.json()['message']


if __name__ =="__main__":
    from gateway import gateway
    lg = gateway().login()
    r1 = ReadJsonData(file="rmProjectSnapshot\\findProjectUser.json").getBody()
    # create = rmProjectLog(s=lg[2]).create(body=r1[0][0],code=r1[0][1],message=r1[0][2],title=r1[0][3])
    lis = rmProjectSnapshot(s=lg[2]).findProjectUser(body=r1[0][0], code=r1[0][1], message=r1[0][2], title=r1[0][3])