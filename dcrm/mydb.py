# Install Mysql on your computer
# https://dev.mysql.com/downloads.installer/
# pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python

import mysql.connector

dataBase =mysql.connector.connect(
    host = 'localhost',
    user ='root',
    password = 'MyNewPass'
    
)

# Prepare a cursor object
cursorObject =dataBase.cursor()

# Create a database 
cursorObject.execute("CREATE DATABASE crmdb")

print("All Done!")