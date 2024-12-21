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
    
def visualdata():
    conn=sqlite3.Connection('lite.db')
    cur=conn.cursor()
    cur.execute("SELECT * FROM data")
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def deletedata(roll):
    conn=sqlite3.Connection('lite.db')
    cur=conn.cursor()
    cur.execute("DELETE FROM data WHERE rollno=?",(roll,))
    conn.commit()
    conn.close()
    
def updatedata(roll,name,mark):
    conn=sqlite3.Connection('lite.db')
    cur=conn.cursor()
    cur.execute("UPDATE data SET name=?,marks=? WHERE rollno=?",(name,mark,roll))
    conn.commit()
    conn.close()

createtable()
insertdata(18,'Janmay',75.0)
print(visualdata())
updatedata(18,'Janmay Bhatt',85)
print(visualdata())
deletedata(18)
print(visualdata())