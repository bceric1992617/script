from sql.sqlconnectionCash import db
db_cur = db.cursor()

db_cur.execute('update interest set 1m=0,2m=0,3m=0,4m=0,5m=0,6m=0,7m=0,8m=0,9m=0,10m=0,11m=0,12m=0;')
db.commit()
