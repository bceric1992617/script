
from sql.sqlconnection import db
db_cur = db.cursor()

db_cur.execute('delete from hot')
db.commit()