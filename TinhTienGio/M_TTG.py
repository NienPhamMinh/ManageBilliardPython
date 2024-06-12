from connectdb import Connection
class ModelTTG:
    def __init__(self):
        self.Ban = []
        self.conn = Connection()
    def loadBan(self):
        self.conn.connect()
        sql_query = """
                SELECT  nameTable, checkIn, checkOut, idstaff, DATE_FORMAT(dateTable,'%d-%m-%Y')
                from tableb
                """
        result = self.conn.query(sql_query)
        self.conn.close()
        return result
    # def update_checkIN(self,id):
    #     self.conn.connect()
    #     sql_query = """
    #             update tableb
    #             set checkIn = now()
    #             where nameTable like '{}'and dateTable =current_date();""".format(id)
    #     self.conn.update(sql_query)
    #     self.conn.close()

    # def reset_checkIN(self,id):
    #     self.conn.connect()
    #     sql_query = """
    #             update tableb
    #             set checkIn = 0
    #             where nameTable like '{}' and dateTable =current_date();""".format(id)
    #     self.conn.update(sql_query)
    #     self.conn.close()
    # cập nhật giờ check out theo mã nv, mã bàn và giờ check in gần nhất
    def update_checkOUT(self,id,nv):
        self.conn.connect()
        sql_query = """
                update tableb
                set checkOut = now()
                where nameTable = '{}'
                and idstaff= '{}' and 
                checkIn = (select max(checkIn) from tableb where nameTable like '{}'and dateTable =current_date() 
                and idstaff= '{}') ;""".format(id,nv,id,nv)
        self.conn.update(sql_query)
        self.conn.close()

    # def reset_checkOUT(self,id):
    #     self.conn.connect()
    #     sql_query = """
    #             update tableb
    #             set checkOut = 0
    #             where nameTable like '{}' and dateTable =current_date();""".format(id)
    #     self.conn.update(sql_query)
    #     self.conn.close()
    # nếu bàn mới trong ngày chưa được check in thì cộng doanh thu mới
    def update_DoanhThu_NUll(self,tienGio,id):
        self.conn.connect()
        sql_query = """
                    update tableb 
                    set incomeDay =  {}
                    where nameTable like '{}' and dateTable = current_date();
                    """.format(tienGio,id)
        self.conn.update(sql_query)
        self.conn.close()
    # Nếu bàn đã được check in trong ngày thì chỉ cộng dồn doanh thu
    def update_DoanhThu_NOT_NUll(self,tienGio,id):
        self.conn.connect()
        sql_query = """
                    update tableb 
                    set incomeDay = incomeDay +{}
                    where nameTable like '{}' and dateTable = current_date();
                    """.format(tienGio,id)
        self.conn.update(sql_query)
        self.conn.close()
    # hàm để kiểm tra doanh thu của bàn trong ngày có chưa
    def checkDoanhThu(self,id):
        self.conn.connect()
        sql_query = """
                    select incomeDay
                    from tableb
                    where nameTable like '{}' and dateTable = current_date();
                    """.format(id)
        result = self.conn.query(sql_query)
        self.conn.close()
        return result
    # hàm để kiểm tra bàn đã được check in lần đầu trong ngày hay chưa
    def checkBan(self,id,nv):
        self.conn.connect()
        sql_query = """
                    select nameTable
                    from tableb
                    where nameTable like '{}' and idstaff like '{}';
                    """.format(id,nv)
        result = self.conn.query(sql_query)
        self.conn.close()
        return result

    # hàm lấy thời gian check out theo giờ check in gần nhất
    def get_checkOut(self,id,nv):
        self.conn.connect()
        sql_query = """
                        SELECT max(checkOut)
                        from tableb
                        where nameTable = '{}' and idstaff like '{}' and
                        checkIn = (select max(checkIn) from tableb where nameTable like '{}' and idStaff like '{}');
                        """.format(id,nv,id,nv)
        result = self.conn.find(sql_query)
        self.conn.close()
        return result

    # hàm lấy giờ check in gần nhất
    def get_checkIn(self,id,nv):
        self.conn.connect()
        sql_query = """
                        SELECT max(checkIn)
                        from tableb
                        where nameTable = '{}' and idstaff like '{}'
                        """.format(id,nv)
        result = self.conn.find(sql_query)
        self.conn.close()
        return result

    # thêm bàn mới
    def insert_Ban(self,idBan,idNV):
        self.conn.connect()
        sql_query = """
                       insert into tableb (nameTable,idstaff,checkIn) 
                        values( '{}','{}',now());
                        """.format(idBan,idNV)
        self.conn.insertData(sql_query)
        self.conn.close()

if __name__ == '__main__':
    model = ModelTTG()
    # model.update_checkIN('Ban03')
    # model.update_checkOUT('Ban02','nv04')
    # model.reset_checkIN('Ban03')
    # model.reset_checkOUT('Ban03')
    # model.update_DoanhThu_NUll(1,'ban02')
    # model.update_DoanhThu_NOT_NUll(1,'ban02')
    print(type(model.get_checkIn('ban02','nv01')[0]))
    if model.get_checkOut('ban02','nv01')[0] is None:
        print('true');
    # model.insert_Ban("Ban01",'NV01')
    # print(model.get_checkIn('Ban03','nv02')[0])
    # print(type(model.get_checkIn('Ban03','nv02')[0]))
    # print(model.checkBan('ban06','nv02'))