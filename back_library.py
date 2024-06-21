import sqlite3
def connect():
    conn = sqlite3.connect(' library.db')
    cur = conn.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY , name text , issue text , auther text , publisher text , serialNo INTEGER , inventory INTEGER )
    ''')
    conn.commit()
    conn.close()

def insert( name , issue , auther , publisher , serialNo , inventory ):
    conn = sqlite3.connect('library.db')
    cur = conn.cursor()
    cur.execute('''
    INSERT INTO books VALUES ( NULL , ? , ? , ? , ? , ? , ? )
    ''' ,( name , issue , auther , publisher , serialNo , inventory ) )
    conn.commit()
    conn.close()
def view():
    conn = sqlite3.connect(' library.db')
    cur = conn.cursor()
    cur.execute('''
    SELECT * FROM books
    ''')
    rows = cur.fetchall()
    conn.close()
    return rows

def search( name = ' ' , issue = ' ' , auther = ' ' , publisher = ' ' , serialNo  = ' ' , inventory = ' ' ):
    conn = sqlite3.connect()
    cur = conn.cursor()
    cur.execute('''
    SELECT * FROM books WHERE  name = ? or issue = ?  or auther = ?  or publisher = ? or serialNo = ?  , inventory = ? 
    ''' , ( name , issue , auther , publisher , serialNo , inventory) )
    rows = cur.fetchall()
    conn.close()
    return rows

def update( id , name , issue , auther , publisher , serialNo , inventory):
    conn = sqlite3.connect()
    cur = conn.cursor()
    cur.execute('''
    UPDATE books SET  name = ? , issue = ?  , authre = ? , publisher = ? , serialNo = ? , inventory = ? WHERE id = ? 
    ''' , ( name , issue , auther , publisher , serialNo , inventory , id ) )
    conn.commit()
    conn.close()



def delete( id ):
    conn = sqlite3.connect()
    cur = conn.cursor()
    cur.execute('''
    DELETE FROM books WHERE  id = ? 
    ''' , ( id , ) )
    conn.commit()
    conn.close()


connect()