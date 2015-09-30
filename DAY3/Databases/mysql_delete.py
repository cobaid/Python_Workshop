from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config

def delete_record(name):
    db_config = read_db_config()

    query = "DELETE FROM test WHERE name = %s"

    try:
        # connect to the database server
        conn = MySQLConnection(**db_config)

        # execute the query
        cursor = conn.cursor()
        cursor.execute(query, (name,))

        # accept the change
        conn.commit()

    except Error as e:
        print "SOMETHING BAD HAPPEND", e

    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    delete_record('test')
