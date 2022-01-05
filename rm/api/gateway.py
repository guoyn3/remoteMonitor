import requests
from common.readIni import ReadIni
from common.readJsonData import ReadJsonData

class gateway():
    def __init__(self,s= requests.session()):
        self.host = ReadIni().getValue(section='host',option='host')
        self.s = s

    def login(self,body={"username": "gtest1", "password": "123456"},code='0',message='成功!',title='账号密码正确，登录成功'):
        url = self.host+'/gateway/login'
        headers = {"content-type":"application/json;charset=UTF-8"}
        json = body
        res = self.s.post(url=url,headers=headers,json=json)
        if res.json()['code'] == '0':
            token = res.json()['data']['token']
            return res.json()['code'], res.json()['message'],self.s,token
        else:
            return res.json()['code'], res.json()['message']

    def logout(self,token=''):
        url = self.host+'/gateway/logout'
        headers = {"Authorization":token}
        res = requests.post(url=url,headers=headers)
        '''if res.json()['message']=='成功!':
            print('token有效，登出成功！')
        else:
            print('token无效，登出失败！')'''

if __name__ == '__main__':
    body = ReadJsonData(file="gateway\\login.json").getBody()
    #lg = gateway().login(body=list(body)[0][0],code=list(body)[0][1],message=list(body)[0][2],title=list(body)[0][3])
    lg = gateway().login()
    #lo = gateway().logout(token=list(lg)[3])

