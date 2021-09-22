import mysql.connector as mysql
import datetime
db = mysql.connect(host="localhost", user="root", password ="", db="coursebot")


#get user data


def enterMood(mood):
    cur = db.cur = db.cursor()
    qry = "INSERT INTO `moodChecker` (date, mood) VALUES (%s, %s)"
    val = (datetime.datetime.now(), mood)
    cur.execute(qry, val)
    db.commit()
    print(cur.rowcount, "record inserted.")
    return True

