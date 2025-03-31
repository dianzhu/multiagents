from database import result1
from database import result2
from database import result3
from database import result4
from database import result5
from database import result6
from database import result7
from database import result8
from database import result9
from database import result10
from database import result11
from database import result12
from database import result13
from database import result14
from database import result15
from database import result16
from database import result17

def contexts(result):
    email = "Can you say for certain that the following emails are spams?"
    i = 1
    for x in result:
        sender = x[0]
        receiver = x[1]
        date = x[2]
        subject = x[3]
        body = x[4]
        email += f"\n({i}) email's sender: {sender}, email's receiver: {receiver}, email's date: {date}, email's subject: {subject}, email's body: {body}"
        i += 1

    return email

email1 = contexts(result1)
email2 = contexts(result2)
email3 = contexts(result3)
email4 = contexts(result4)
email5 = contexts(result5)
email6 = contexts(result6)
email7 = contexts(result7)
email8 = contexts(result8)
email9 = contexts(result9)
email10 = contexts(result10)
email11 = contexts(result11)
email12 = contexts(result12)
email13 = contexts(result13)
email14 = contexts(result14)
email15 = contexts(result15)
email16 = contexts(result16)
email17 = contexts(result17)


