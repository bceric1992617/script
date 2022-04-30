from sql.sqlconnectionCash import db
db_cur = db.cursor()

db_cur.execute('update interest set today=0;')
db.commit()
