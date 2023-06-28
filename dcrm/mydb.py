import mysql.connector

dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Admin@123'
)

# prepare a cursor object
curserObject = dataBase.cursor()

# create a database
curserObject.execute("CREATE DATABASE dcrmdb")
print("All Done!")
