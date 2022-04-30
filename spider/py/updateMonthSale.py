from sql.sqlconnectionCash import db
db_cur = db.cursor()

db_cur.execute('update menu set monthSaleNum=0;')
db.commit()
