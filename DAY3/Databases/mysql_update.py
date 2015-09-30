from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config

def update_records(name, classNM):
    db_config = read_db_config()

    query = "update test set class = %s where name=%s "

    data = (classNM, name)
    try:
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, data)

        conn.commit()
    except Error as e:
        print "[SOMETHING BAD HAPPEND]", e

    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    update_records('zain', 'ME')
