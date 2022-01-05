from common.connectMysql import ConnectMysql

class GetMysqlValues():
    def __init__(self,sql= "SELECT * FROM `gcp_rm`.`rm_project_log` WHERE `project_id` = '239' AND `log_type` = '3' ORDER BY `create_time` DESC",size = 5):
        db = ConnectMysql()
        self.res = db.selectSql(sql,size)
        length = len(self.res)
        if length < size:
            self.size = length
        else:
            self.size = size
        #print(self.size)
        #print(self.res)
        #print(type(self.res[0]))
        self.list_data = []

    def getkeys(self):
        key_dict = self.res[0]
        #print(key_dict)
        #print(type(key_dict))
        key = list(key_dict.keys())[0]
        #print(key)
        return key

    def getValues(self):
        for i in range(self.size):
            k = self.res[i][self.getkeys()]
            #print(k)
            self.list_data.append(k)
        print(self.list_data)
        return self.list_data

if __name__ == '__main__':
    gv = GetMysqlValues()
    gv.getkeys()
    gv.getValues()


#     def select_sql(self,sql= "select username from pms_users",size =5):
#         self.cursor.execute(sql)
#         res = self.cursor.fetchmany(size)
#         #print(type(res))
#         key_dict = res[0]
#         print(key_dict)
#         key = list(key_dict.keys())[0]
#         print(key)
#         #print(res)
#         list_data = []
#         for i in range(len(res)):
#             colu = res[i][key]
#             print(colu)
#             list_data.append(colu)
#         #print(list_data)
#         return list_data
#
#     def update_sql(self,sql= "update pms_projects set name='更新项目名' where userid = '653700466378543104' limit 1",size =5):
#         self.cursor.execute(sql)
#         self.con.commit()
#
# if __name__ == '__main__':
#     conn = ConnectMysql()
#     conn.select_sql()
#     #conn.update_sql()