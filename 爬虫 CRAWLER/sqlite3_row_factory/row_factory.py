import sqlite3
conn = sqlites.connect(r'e:\sql\bookstore.db')
c = conn.cursor()
sql = 'select * from book'
result = c.execute(sql)
result.fetchall()

def dict_factory(cursor, row):
	d = {}
	for i, col in enumerate(cursor.description):
		d[col[0]]=row[i]
	return d 

conn = sqlite3.connect(r'e:\sql\bookstore.db')
conn.row_factory = dict_factory
c = conn.cursor()
c.execute(sql).fetchall()

results = c.execute(sql).fetchall()
for row in results:
	print(row.get('Author'),row['Price'])
