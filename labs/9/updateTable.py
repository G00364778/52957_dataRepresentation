import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  #user="datarep",  # this is the user name on my mac
  #passwd="password" # for my mac
  database="datarep"
)

cursor = db.cursor()
sql="update student set name= %s, age=%s  where id = %s"
values = ("John",33, 1)

cursor.execute(sql, values)

db.commit()
print("update done")