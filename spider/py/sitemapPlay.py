import time
import math
from sql.sqlconnection import db
db_cur = db.cursor()

db_cur.execute("select count(*) from bajiecaiji")
count = db_cur.fetchone()

num = 50000 #每次多少行
for i in range(math.ceil(count[0]/num)):
    page = i * num #页
    db_cur.execute("select filmsId,playAddrId,linkType from bajiecaiji order by playAddrId desc limit "+ str(page) +","+ str(num) +";")
    arrList = db_cur.fetchall()
    f=open("txtfile/playsitemap"+ str(i+1) +".txt","w")
    url = "https://www.yangbaicaidy.com/play/"
    yunUrlStr = ""
    for v in arrList:
        if v[2] == 1:
            type = 'k'
        else:
            type = 'm'
        f.write(yunUrlStr + url + str(v[0]) + '-' + str(v[1]) + '-' + type + '\n')

f.close

