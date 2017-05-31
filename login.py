import MySQLdb
from connect import connect

def login(email, password):
  db = connect()
  cur = db.cursor()
  cur.execute("SELECT * from users WHERE email=%s", (email,))
  for row in cur.fetchall():
    if password == row[2]:
      db.close()
      return True

  db.close()
  return False
