import requests
from common.readIni import ReadIni
from common.readJsonData import ReadJsonData


class rmMessage():
    def __init__(self, s=requests.session()):
        self.s = s
        self.host = ReadIni().getValue(section="host", option='host')

    def create(self, body="您收到了gtest1(GCP)的受试者信息申请，请您查看。", createTime="2021-12-12 12:12:12",
               header='{"jumpType": "SUBJECT_APPROVAL", "projectId": 239, "subjectId": 1657, "subjectApplyId": 1462974935490670593}',
               receiver="1462974935490670593", title="测试"):
        url = self.host + '/api/gcp-rm/rmMessage/create'
        headers = {"content-type": "application/json;charset=UTF-8"}
        json = {
            "body": body,
            "createTime": createTime,
            "header": header,
            "id": "",
            "isRead": 0,
            "receiver": receiver,
            "sender": receiver,
            "tenantCode": "",
            "title": title,
            "type": 1
        }
        res = self.s.post(url=url, headers=headers, json=json)
        return res.json()['code'], res.json()['message']

    def findByPage(self, body='', code='0', message='成功!', title='查询消息成功'):
        url = self.host + '/api/gcp-rm/rmMessage/findByPage'
        headers = {"content-type": "application/json;charset=UTF-8"}
        json = body
        res = self.s.post(url=url, headers=headers, json=json)
        return res.json()['code'], res.json()['message']

    def queryCount(self, body='', code='', message='', title=''):
        url = self.host + '/api/gcp-rm/rmMessage/queryCount'
        headers = {"content-type": "application/json;charset=UTF-8"}
        json = body
        res = self.s.post(url=url, headers=headers, json=json)
        return res.json()['code'], res.json()['message']

    def read(self, body='', code='', message='', title=''):
        url = self.host + '/api/gcp-rm/rmMessage/read'
        headers = {"content-type": "application/json;charset=UTF-8"}
        json = body
        res = self.s.post(url=url, headers=headers, json=json)
        return res.json()['code'], res.json()['message']

    def readAll(self, body='', code='', message='', title=''):
        url = self.host + '/api/gcp-rm/rmMessage/readAll'
        headers = {"content-type": "application/json;charset=UTF-8"}
        json = body
        res = self.s.post(url=url, headers=headers, json=json)
        return res.json()['code'], res.json()['message']


if __name__ == '__main__':
    from rm.api.gateway import gateway

    create_body = ReadJsonData(file="rmMessage\\readAll.json").getBody()
    lg = gateway().login()
    cr = rmMessage(s = list(lg)[2]).readAll(body=list(create_body)[0][0], code=list(create_body)[0][1], message=list(create_body)[0][2], title=list(create_body)[0][3])
    #cr = rmMessage(s=list(lg)[2]).create()
