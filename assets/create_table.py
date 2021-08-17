import mysql.connector as msc

def create_table():
    mydb = msc.connect(host="sql6.freemysqlhosting.net", user="sql6429073", passwd='8uMGp8HslA', database='sql6429073')
    mycursor = mydb.cursor()
    sql = "CREATE TABLE if not exists people(s_id int(5) PRIMARY KEY,name varchar(25),email varchar(20),password varchar(10),date_of_birth date,gender varchar(1));"
    mycursor.execute(sql)
    print("\t\ttable created")

create_table()

