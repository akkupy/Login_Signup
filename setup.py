from assets.create_table import *
from assets.credentials import *
import time,sys,os
try:
    os.system('pip install -r requirements.txt')
except:
    print("Check if python and pip is installed correctly!")
    print("Aborting Setup...")
    time.sleep(2)
    sys.exit()

os.environ['host']=input("Enter the Mysql Host Name :")
os.environ['user']=input("Enter the Mysql User Name :")
os.environ['password']=input("Enter the Mysql Password :")
os.environ['database']=input("Enter the Database Name :")

choice=input("Do you wish to create a new table for user information?(y/n) :")

if choice=='y':
    ak=create_table(host,user,password,database)
    if ak:
        print("Table created for User Information.")
    else:
        print("Invalid credentials.")
        print("Aborting Setup...")
        time.sleep(2)
        sys.exit()
elif choice=='n':
    os.system('python app.py')
    time.sleep(3)
    sys.exit()
