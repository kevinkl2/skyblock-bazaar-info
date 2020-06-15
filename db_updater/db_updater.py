import time
import mysql.connector

mydb = mysql.connector.connect(
  host="mysql_db_container",
  user="root",
  password="example"
)

print(mydb, flush=True)

while(True):
    time.sleep(1)
    print("test", flush=True)