import os
from configparser import ConfigParser
import json


class ReadJsonData():
    def __init__(self, file="gateway\\login.json"):
        path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        self.json_path = os.path.join(path, 'data_json', file)

    def getBody(self):
        with open(self.json_path, "r", encoding="utf8") as fp:
            json_data = json.load(fp)
        #list = []
        value_list = []
        if isinstance(json_data, dict):  # 判断是否是字典类型isinstance 返回True false
            for key in json_data:
                if isinstance(json_data[key], dict):  # 如果json_data[key]依旧是字典类型
                    #list.append(json_data[key])
                    tu = tuple(json_data[key].values())
                    value_list.append(tu)
                else:
                    # print("****key--：%s value--: %s" % (key, json_data[key]))
                    str = json_data[key]
            # print(list)
            # print(value_list)
            # print(stri)
            return value_list


if __name__ == '__main__':
    x = ReadJsonData().getBody()
    # print(list(x)[0][0]) #取body
    # print(list(x)[0][1])  # 取code
