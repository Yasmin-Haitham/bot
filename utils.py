import mysql.connector as mysql
conn = mysql.connect(host="localhost", user="root", password ="", db="coursebot")


#get user data

def getUser(user):
    cur = conn.cursor(dictionary=True)
    qry = "SELECT * FROM `user` WHERE `username`='{}'".format(user)

#set user data

