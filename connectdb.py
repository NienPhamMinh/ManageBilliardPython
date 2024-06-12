import mysql.connector
from mysql.connector import Error
class Connection:
    def __init__(self,user='root',password='123456',host ='localhost',database='mydb'):
        self.user = user
        self.password = password
        self.host = host
        self.database = database
        self.connection = None
    def connect(self):
        try:
            self.connection = mysql.connector.connect(user=self.user,password=self.password,host=self.host,database=self.database)
            print('Connection successful')
            # if self.connecttion.is_connected():
            #     db = self.connection.get_server_info()
            #     print('Connect to Mysql Server',db)
            #     cursor = sel.connection.cursor()
            #     cursor.execute('select * from manager ;')
            #     record = cursor.fetchall()
            #     for result in record:
            #         print(result)
        except Error as e:
            print('Error while connecting to database',e)
    def query(self,sql):
        cursor = self.connection.cursor()
        cursor.execute(sql)
        return cursor.fetchall()
    def update(self,sql):
        cursor = self.connection.cursor()
        cursor.execute(sql)
        self.connection.commit()
    def deleteData(self,sql):
        cursor = self.connection.cursor()
        cursor.execute(sql)
        self.connection.commit()
    def insertData(self,sql):
        cursor = self.connection.cursor()
        cursor.execute(sql)
        self.connection.commit()

    def find(self,sql):
        cursor = self.connection.cursor()
        cursor.execute(sql)
        return cursor.fetchone()

    def close(self):
        if self.connection.is_connected():
            # cursor.close()
            self.connection.close()
            print('Connection closed')
