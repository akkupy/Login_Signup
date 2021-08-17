import mysql.connector as msc

def create_table():
    mydb = msc.connect(host="db4free.net", user="akku1234", passwd='akku4321', database='testakku1234')
    mycursor = mydb.cursor()
    sql = "CREATE TABLE if not exists people(s_id int(5) PRIMARY KEY,name varchar(25),email varchar(20),password varchar(10),date_of_birth date,gender varchar(1));"
    mycursor.execute(sql)
    print("\t\ttable created")

create_table()

