"""
5 step way

c=connection
c=cursor
execute
c=commit
c=close

Focusing on , and ?
Functions usage
"""
import sqlite3

def createtable():
    conn=sqlite3.Connection('lite.db')
    cur=conn.cursor()
    cur.execute("CREATE TABLE data(rollno INTEGER, name TEXT, marks REAL)")
    conn.commit()
    conn.close()

createtable()