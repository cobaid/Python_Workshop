from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config

def insert_One(name, classNM, skills):
    query = "insert into test(name, class, skills) values(%s, %s, %s)"
    args = (name, classNM, skills)

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, args)
        if (cursor.lastrowid):
            print 'last insert id: ', cursor.lastrowid
        else:
            print 'last insert id not found'
        conn.commit()
    except Error as e:
        print "[SOMETHING BAD HAPPEND!]",e

    finally:
        cursor.close()
        conn.close()

def insert_many(entry):
    query = "insert into test(name, class, skills) values(%s, %s, %s)"
    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.executemany(query, entry)
        conn.commit()
    except Error as e:
        print "[SOMETHING BAD HAPPEND!]",e
    finally:
        cursor.close()
        conn.close()

if __name__  == '__main__':
    #insert_One('Amir', 'Facuilty', 'C java python android')
    entry = [ ('sameer', 'faculty', 'scilab'), ('javed', 'faculty', 'PHP')]

    insert_many(entry)
