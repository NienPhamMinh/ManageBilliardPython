from connectdb import Connection
class Model_TDT:
    def __init__(self):
        self.QuanLy = []
        self.NhanVien = []
        self.conn = Connection()


    def LoadDoanhThu(self):
        self.conn.connect()
        sql_query = """
                    select DATE_FORMAT(dateTable,'%d-%m-%Y'), round(sum(incomeDay),2)
                    from tableb
                    group by dateTable;
        """
        result = self.conn.query(sql_query)
        self.conn.close()
        return result

    def DoanhThuThang(self):
        self.conn.connect()
        sql_query ="""
                   select round(sum(incomeDay),2)
                   from tableb
                   where month(dateTable)= month(curdate())
                   """
        result = self.conn.query(sql_query)
        self.conn.close()
        return result

    def TongLuong(self):
        self.conn.connect()
        sql_query="""
                select round(sum(Luong),1)
                from staff
        """
        result = self.conn.query(sql_query)
        self.conn.close()
        return  result



if __name__ == '__main__':
    model = Model_TDT()
    print(model.LoadDoanhThu())
