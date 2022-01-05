import requests
from common.readIni import ReadIni
from common.readJsonData import ReadJsonData

class syncData():
    def __init__(self,s=requests.session()):
        self.s=s
        self.host = ReadIni().getValue(section='host', option='host')

    def process(self):
        url = self.host + '/api/gcp-rm/syncData/process'
        headers = {"Content-Type": "application/json;charset=UTF-8"}
        res = self.s.post(url=url, headers=headers)
        return res.json()['code'], res.json()['message']

if __name__ =="__main__":
    pass