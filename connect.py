import MySQLdb

def connect():
  return MySQLdb.connect(host="localhost",
                         user="root",
			 passwd="ubuntu",
			 db="snippets-storage")

