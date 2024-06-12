from connectdb import Connection
class ModelQLNV:
    def __init__(self):
        self.QuanLy = []
        self.NhanVien = []
        self.conn = Connection()
    def loadNV(self):
        self.conn.connect()
        sql_query = """
                SELECT * 
                from staff 
                """
        result = self.conn.query(sql_query)
        self.conn.close()
        return result
    # cập nhật ngày làm việc cho nhân viên
    def update_workDay_NV(self,workDay,id):
        self.conn.connect()
        sql_query = """
                update staff
                set workDay = '{}' 
                where idStaff like '{}';""".format(workDay,id)
        self.conn.update(sql_query)
        self.conn.close()
    # cập nhật lương cho nhân viên
    def update_Luong_NV(self,id):
        self.conn.connect()
        sql_query = "update staff set Luong = ( select workDay from staff where idStaff ='"+id+"')* 200000 where idStaff = '"+id+"';"

        self.conn.update(sql_query)
        self.conn.close()
    def delete_NV(self,id):
        self.conn.connect()
        sql_query = """
                        delete from staff where idStaff = '{} ';""".format(id)
        result = self.conn.deleteData(sql_query)
        self.conn.close()
        return result
    def insert_NV(self,id,name,password):
        self.conn.connect()
        sql_query = """
                       insert into staff (idStaff,nameStaff,passwordStaff) 
                        values( '{}','{}',{});
                        """.format(id,name,password)
        self.conn.insertData(sql_query)
        self.conn.close()


    # def find_KH(self,phone):
    #     self.conn.connect()
    #     sql_query = """
    #                     SELECT *
    #                     from customer
    #                     where phone = '{}'
    #                     """.format(phone)
    #     result = self.conn.find(sql_query)
    #     self.conn.close()
    #     return result


if __name__ == '__main__':
    nv = ModelQLNV()
    # nv.update_name_KH('Tran Tuan Tu','0123456711')
    # nv.insert_KH('0981862763','Nguyen Thi An','1988/07/24')
    # nv.delete_KH('0123456714')
    nv.insert_NV('NV02','Trần Văn Cung',1234,26)
    # nv.loadNV()
    print(nv.loadNV())
