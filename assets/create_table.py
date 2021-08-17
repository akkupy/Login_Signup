import mysql.connector as msc

def create_table(host,user,password,database):
    try:
        mydb = msc.connect(host=host, user=user, passwd=password, database=database)
        mycursor = mydb.cursor()
        sql = "CREATE TABLE if not exists people(s_id int(5) PRIMARY KEY,name varchar(25),email varchar(20),password varchar(10),date_of_birth date,gender varchar(1));"
        mycursor.execute(sql)
        return True
    except:
        return False
    


