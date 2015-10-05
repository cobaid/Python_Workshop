from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config

def query_with_fetchone():
	print "FetchOne..........."
	try:
		db_config = read_db_config()
		conn  = MySQLConnection(**db_config)
		cursor = conn.cursor()
		cursor.execute('select * from test')

		row  = cursor.fetchone()

		while row is not None:
			print row
			row = cursor.fetchone()
	except Error as e:
		print "[SOMETHING BAD HAPPEND ]", e
	finally:
		conn.close()
		cursor.close()

def query_with_fetchall():
	print "FetchAll..........."
	try:
		db_config = read_db_config()
		conn  = MySQLConnection(**db_config)
		cursor = conn.cursor()
		cursor.execute('select * from test')

		rows  = cursor.fetchall()

		for row in rows:
			print row
	except Error as e:
		print "[SOMETHING BAD HAPPEND ]", e
	finally:
		conn.close()
		cursor.close()


def query_with_fetchmany():
	print "FetchMany...........\n"
	try:
		db_config = read_db_config()
		conn  = MySQLConnection(**db_config)
		cursor = conn.cursor()
		cursor.execute('select * from test')

		for row in iter_rows(cursor, 10):
			print row
	except Error as e:
		print "[SOMETHING BAD HAPPEND ]", e
	finally:
		conn.close()
		cursor.close()

def iter_rows(cursor, size=10):
	while  True:
		rows = cursor.fetchmany(10)
		if not rows:
			break
		for row in rows:
			yield row

if __name__ == '__main__':
	query_with_fetchone()
	query_with_fetchall()
	query_with_fetchmany()
