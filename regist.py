import MySQLdb
from connect import connect

def regist(email, password):
  db = connect()
  cur = db.cursor()
  try:
    cur.execute("SELECT * FROM users WHERE email=%s", (email,))
    if cur.rowcount > 0:
      return False
    cur.execute("INSERT INTO users (email, password) VALUES (%s, %s)", (email, password))
    db.commit()
    db.close()
    return True
  except:
    db.rollback()
    db.close()
    return False

