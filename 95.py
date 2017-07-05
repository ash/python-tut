import MySQLdb

db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="",           # your password
                     db="testparis")      # name of the data base

# you must create a Cursor object. It will let
# you execute all the queries you need
cur = db.cursor()

new_data = {'id': 200, 'name': 'Andrew'}
cur.execute('insert into data values(%(id)s, %(name)s)', new_data)
db.commit()

# Use all the SQL you like
cur.execute("select * from data")

# print all the first cell of all the rows
for row in cur.fetchall():
    print(int(row[0]), row[1])

db.close()
