import pymysql
from common.readIni import ReadIni

class ConnectMysql():
    def __init__(self,database = 'gcp_rm'):
        dbinfo = ReadIni().getValue('dbinfo','gcp_rm')
        #print(type(dbinfo))
        db = eval(dbinfo)    #str转换为dict
        #print(db)
        #print(type(db))
        self.con = pymysql.connect(database=database,
                                   cursorclass = pymysql.cursors.DictCursor,
                                   **db)
        self.cursor = self.con.cursor()

    def selectSql(self,sql,size=1):
        self.cursor.execute(sql)
        res = self.cursor.fetchmany(size)
        #print(res)
        return res


    def updateSql(self,sql):
        self.cursor.execute(sql)
        self.con.commit()
        #self.cursor.close()
        #self.con.close()


    def deleteSql(self,sql):
        self.cursor.execute(sql)
        self.con.commit()

    def insertSql(self, sql, data):
        self.cursor.execute(sql,data)
        self.con.commit()

if __name__ =='__main__':
    conn = ConnectMysql()
    #conn.selectSql(sql = "SELECT * FROM `gcp_rm`.`rm_project_log` WHERE `project_id` = '239' AND `log_type` = '3' ORDER BY `create_time` DESC",size =1)
    #conn.updateSql()
    import time
    project_no = time.strftime("%Y%m%d_%H%M%S")
    ti = time.strftime("%Y-%m-%d 00:00:00")
    sql = "INSERT INTO `gcp_rm`.`mid_project`(`id`, `project_no`, `project_name`, `spons_name`, `cro_spons_name`, `main_researcher_name`, `trial_phase`, `trial_method`, `test_object_name`, `indications`, `belong_specialty`, `trial_create_time`, `trial_start_date`, `trial_end_time`, `check_name`, `tenant_code`, `create_date_time`, `create_user_id`, `update_date_time`, `update_user_id`, `project_status`, `check_time`) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    data = (
    '1', project_no, project_no, '11', '22', '33', '44', '55', '66', '77', '88', ti, ti, None, None, None, None, None,
    None, None, 2, None)
    i = conn.insertSql(sql=sql, data=data)
    s = ConnectMysql().selectSql(sql="select * from mid_project",size=1)
    print(s)