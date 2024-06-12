from connectdb import Connection

class ModelDN:
    def __init__(self):
        self.QuanLy =[]
        self.NhanVien =[]
        self.conn = Connection()
    # kiểm tra đăng nhập của NV và QL
    def DangNhap_NV(self,id,password):
        self.conn.connect()
        sql_query = """
        SELECT * 
        from staff
        where idStaff like '{}' AND passwordStaff like '{}'""".format(id,password)
        result = self.conn.query(sql_query)
        self.conn.close()
        return result
    def DangNhap_QL(self,id,password):
        self.conn.connect()
        sql_query = """
        SELECT passwordManager 
        from manager 
        where idManager like '{}' AND passwordManager like '{}'""".format(id,password)
        result = self.conn.query(sql_query)
        self.conn.close()
        return result
if __name__ == '__main__':
    id = 'QL01'
    passw = 1234
    c = ModelDN()
    result = c.DangNhap_QL(id,passw)

    print(result)
