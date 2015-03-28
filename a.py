import secure_password
import connection


db = connection.connection()
conn = db.connect()
cur = conn.cursor()
cur.execute('select password from user where userName=%s', 'user1') 
for rs in cur.fetchall():
	print(rs[0])
	print(secure_password.validate_password(rs[0], 'abc123456'))
	print(len(rs[0]))
conn.commit()
cur.close()
conn.close()