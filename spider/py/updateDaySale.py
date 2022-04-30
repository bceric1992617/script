from sql.sqlconnectionCash import db
db_cur = db.cursor()

db_cur.execute('update menu set daySaleNum=0;')
db.commit()
