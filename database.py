import mysql.connector

from dataset import file1
from dataset import file2
from dataset import file3
from dataset import file4
from dataset import file5
from dataset import file6
from dataset import file7

mydb = mysql.connector.connect(
    host="localhost",
    user="cs6400_db",
    password="vA19qv1Q*u[b",
    database="mydb"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE IF NOT EXISTS firsttable (number INT, sender VARCHAR(255), receiver VARCHAR(255), dates VARCHAR(255), subject VARCHAR(255), body LONGTEXT, PRIMARY KEY(number))")

def insertdata(files):
    for col in files:
        sql = "INSERT INTO firsttable (number,sender,receiver,dates,subject,body) VALUES (%s,%s,%s,%s,%s,%s) ON DUPLICATE KEY UPDATE sender = VALUES(sender), receiver = VALUES(receiver), dates = VALUES(dates), subject = VALUES(subject), body = VALUES(body)"
        val = (col['number'], col['sender'],col['receiver'],col['date'],col['subject'],col['body'])
        mycursor.execute(sql, val)

insertdata(file1)
insertdata(file2)
insertdata(file3)
insertdata(file4)
insertdata(file5)
insertdata(file6)
insertdata(file7)

mydb.commit()

def selectdata(i):
    mycursor.execute(f"SELECT sender, receiver, dates, subject, body FROM firsttable limit {i}, 6")

selectdata(0)
result1 = mycursor.fetchall()

selectdata(6)
result2 = mycursor.fetchall()

selectdata(12)
result3 = mycursor.fetchall()

selectdata(18)
result4 = mycursor.fetchall()

selectdata(24)
result5 = mycursor.fetchall()

selectdata(30)
result6 = mycursor.fetchall()

selectdata(36)
result7 = mycursor.fetchall()

selectdata(42)
result8 = mycursor.fetchall()

selectdata(48)
result9 = mycursor.fetchall()

selectdata(54)
result10 = mycursor.fetchall()

selectdata(60)
result11 = mycursor.fetchall()

selectdata(66)
result12 = mycursor.fetchall()

selectdata(72)
result13 = mycursor.fetchall()

selectdata(78)
result14 = mycursor.fetchall()

selectdata(84)
result15 = mycursor.fetchall()

selectdata(90)
result16 = mycursor.fetchall()

selectdata(96)
result17 = mycursor.fetchall()


