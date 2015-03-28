import secure_password
import connection


data = secure_password.encrypt_password("abc123456", None)
print('%s' % data)
print(len(data))
db = connection.connection()
conn = db.connect()
cur = conn.cursor()
print(cur.execute('update user set password=%s where userName="user1"', data))
conn.commit()
cur.close()
conn.close()
