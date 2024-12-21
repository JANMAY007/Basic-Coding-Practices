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

print(visualdata())