# import pyodbc
# import sys

# def read(conn):
#   print('Read')
#   cursor = conn.cursor()
#   cursor.execute('select * from Skills')
#   for row in cursor:
#     print(f'row = { row }')
#   print()

# def create(conn):
#   print('Create')
#   cursor = conn.cursor()
#   cursor.execute(
#     'insert into Skills(skills, level) values(?,?);', 
#     ('React', 'Master')
#   )
#   conn.commit()
#   read(conn)

# def update(conn):
#   print('Update')
#   cursor = conn.cursor()
#   cursor.execute(
#     'update Skills set skills = ? where level = ?;', 
#     ('MongoBD', 'Master')
#   )
#   conn.commit()
#   read(conn)

# def delete(conn):
#   print('Delete')
#   cursor = conn.cursor()
#   cursor.execute(
#     'delete from Skills where ID > 1 '
#   )
#   conn.commit()
#   read(conn)

# conn = pyodbc.connect(
#   "Driver={SQL Server Native Client 11.0};"
#   "Server=BINHKN\SQLEXPRESS;"
#   "Database=BlogBK;"
#   "Trusted_Connection=yes;"
# )

# read(conn)
# create(conn)
# update(conn)
# delete(conn)

# conn.close()
