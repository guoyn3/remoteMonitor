import requests
from common.readIni import ReadIni
from common.readJsonData import ReadJsonData
import time


class rmApproval():
    def __init__(self, s=requests.session()):
        self.s = s
        self.host = ReadIni().getValue(section='host', option='host')

    def create(self, body="",code="",message="",title=""):
        url = self.host + '/api/gcp-rm/rmApproval/create'
        headers = {"content-type": "application/json;charset=UTF-8"}
        json = body
        res = self.s.post(url=url, headers=headers, json=json)
        return res.json()['code'], res.json()['message']

    def deleteById(self, id=''):
        url = self.host + '/api/gcp-rm/rmApproval/deleteById'
        headers = {"content-type": "application/json;charset=UTF-8"}
        json = {
            "id":id
        }
        res = self.s.post(url=url, headers=headers, json=json)
        return res.json()['code'], res.json()['message']

    def findById(self, id="1040"):
        url = self.host + '/api/gcp-rm/rmApproval/findById'
        headers = {"content-type": "application/json;charset=UTF-8"}
        json = {
            "id": id
        }
        res = self.s.post(url=url, headers=headers, json=json)
        return res.json()['code'], res.json()['message']

    def findByPage(self, body='', code='', message='', title=''):
        url = self.host + '/api/gcp-rm/rmApproval/findByPage'
        headers = {"content-type": "application/json;charset=UTF-8"}
        json = body
        res = self.s.post(url=url, headers=headers, json=json)
        return res.json()['code'], res.json()['message']

    def update(self, body='', code='', message='', title=''):
        url = self.host + '/api/gcp-rm/rmApproval/update'
        headers = {"content-type": "application/json;charset=UTF-8"}
        json = body
        res = self.s.post(url=url, headers=headers, json=json)
        return res.json()['code'], res.json()['message']

    def monitorPass(self, id="", projectId="242"):
        url = self.host + '/api/gcp-rm/rmApproval/monitorPass'
        headers = {"content-type": "application/json;charset=UTF-8"}
        json = {
            "id": id,
            "projectId": projectId,
        }
        res = self.s.post(url=url, headers=headers, json=json)
        return res.json()['code'], res.json()['message']

    def monitorRefuse(self, id="", projectId="242", desc="远程监查审批不通过"):
        url = self.host + '/api/gcp-rm/rmApproval/monitorRefuse'
        headers = {"content-type": "application/json;charset=UTF-8"}
        json = {
            "id": id,
            "projectId": projectId,
            "desc": desc
        }
        res = self.s.post(url=url, headers=headers, json=json)
        return res.json()['code'], res.json()['message']

    def projectPass(self, id='233', desc='项目审批通过'):
        url = self.host + '/api/gcp-rm/rmApproval/projectPass'
        headers = {"content-type": "application/json;charset=UTF-8"}
        json = {
            "id":id,
            "desc":desc
        }
        res = self.s.post(url=url, headers=headers, json=json)
        return res.json()['code'], res.json()['message']

    def subjectPass(self, id="", projectId="242", desc="受试者审批通过"):
        url = self.host + '/api/gcp-rm/rmApproval/subjectPass'
        headers = {"content-type": "application/json;charset=UTF-8"}
        json = {
            "id": id,
            "projectId": projectId,
            "desc": desc
        }
        res = self.s.post(url=url, headers=headers, json=json)
        return res.json()['code'], res.json()['message']

    def subjectRefuse(self, id="", projectId="242", desc="受试者审批不通过"):
        url = self.host + '/api/gcp-rm/rmApproval/subjectRefuse'
        headers = {"content-type": "application/json;charset=UTF-8"}
        json = {
            "id": id,
            "projectId": projectId,
            "desc": desc
        }
        res = self.s.post(url=url, headers=headers, json=json)
        return res.json()['code'], res.json()['message']

    def subjectCancel(self, id="", projectId="242"):
        url = self.host + '/api/gcp-rm/rmApproval/subjectCancel'
        headers = {"content-type": "application/json;charset=UTF-8"}
        json = {
            "id": id,
            "projectId": projectId
        }
        res = self.s.post(url=url, headers=headers, json=json)
        return res.json()['code'], res.json()['message']

    def monitorApplyNumber(self):
        url = self.host + '/api/gcp-rm/rmApproval/monitorApplyNumber'
        headers = {"content-type": "application/json;charset=UTF-8"}
        res = self.s.post(url=url, headers=headers)
        return res.json()['code'], res.json()['message']

    def startProjectNumber(self):
        url = self.host + '/api/gcp-rm/rmApproval/startProjectNumber'
        headers = {"content-type": "application/json;charset=UTF-8"}
        res = self.s.post(url=url, headers=headers)
        return res.json()['code'], res.json()['message']

    def process(self, body='', code='', message='', title=''):
        url = self.host + '/api/gcp-rm/rmApproval/process'
        headers = {"content-type": "application/json;charset=UTF-8"}
        json = body
        res = self.s.post(url=url, headers=headers, json=json)
        return res.json()['code'], res.json()['message']


if __name__ == "__main__":
    from rm.api.gateway import gateway

    lg = gateway().login()
    from common.readJsonData import ReadJsonData

    body = ReadJsonData(file='rmApproval\\create.json').getBody()
    # print(body)
    cr = rmApproval(s=list(lg)[2]).create(body=list(body)[1][0], code=list(body)[1][1], message=list(body)[1][2],
                                          title=list(body)[1][3])
