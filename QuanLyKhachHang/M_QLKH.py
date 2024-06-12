from connectdb import Connection
class ModelQLKH:
    def __init__(self):
        self.QuanLy = []
        self.NhanVien = []
        self.conn = Connection()
    # lấy dữ liệu khách hàng
    def loadKH(self):
        self.conn.connect()
        sql_query = """
                SELECT * 
                from customer 
                """
        result = self.conn.query(sql_query)
        self.conn.close()
        return result
    def update_name_KH(self,name,phone):
        self.conn.connect()
        sql_query = """
                update customer
                set name = '{}' 
                where phone like '{}';""".format(name,phone)
        self.conn.update(sql_query)
        self.conn.close()
    def delete_KH(self,phone):
        self.conn.connect()
        sql_query = """
                        delete from customer where phone= {} ;""".format(phone)
        result = self.conn.deleteData(sql_query)
        self.conn.close()
        return result
    def insert_KH(self,phone,name,dob):
        self.conn.connect()
        sql_query = """
                       insert into customer (phone,name,dob) 
                        values( '{}','{}', date_format( str_to_date("{}",'%d-%m-%Y'), '%y-%m-%d'));
                        """.format(phone,name,dob)
        self.conn.insertData(sql_query)
        self.conn.close()

    # Tìm khách hàng theo số điện thoại
    def find_KH(self,phone):
        self.conn.connect()
        sql_query = """
                        SELECT * 
                        from customer 
                        where phone = '{}'
                        """.format(phone)
        result = self.conn.find(sql_query)
        self.conn.close()
        return result


if __name__ == '__main__':
    nv = ModelQLKH()
    # nv.update_name_KH('Tran Tuan Tu','0123456711')
    # nv.insert_KH('0981862763','Nguyen Thi An','1988/07/24')
    # nv.delete_KH('0123456714')

    nv.loadKH()
    print(nv.loadKH())
