import sqlite3

def createtable():
    conn=sqlite3.Connection('lite.db')
    cur=conn.cursor()
    cur.execute("CREATE TABLE data(rollno INTEGER, name TEXT, marks REAL)")
    conn.commit()
    conn.close()
    
def insertdata(roll,name,mark):
    conn=sqlite3.Connection('lite.db')
    cur=conn.cursor()
    cur.execute("INSERT INTO data VALUES(?,?,?)",(roll,name,mark))
    conn.commit()
    conn.close()

roll=int(input())
name=input()
mark=float(input())
createtable()
insertdata(roll,name,mark)