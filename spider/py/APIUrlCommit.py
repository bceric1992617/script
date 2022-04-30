
import time
import math
from sql.sqlconnection import db
db_cur = db.cursor()
db_cur.execute("select count(*) from films;")
count = db_cur.fetchone()

limit = 2000
for i in range(math.ceil(count[0] / limit)):
    page = i * limit #页数
    db_cur.execute("select filmsId from films order by filmsId limit "+ str(page) +","+ str(limit) +";")
    filmMsg = db_cur.fetchall()
    f=open("txtfile/APIUrlCommit/APIUrlCommit"+ str(i+1) +".txt","w")
    for v in filmMsg :
        url = 'https://www.yangbaicaidy.com/detail/' + str(v[0]) + '\n'
        f.write(url)

    f=open("txtfile/APIUrlCommit/APIUrlCommand.txt","a")
    f.write("curl -H 'Content-Type:text/plain' --data-binary @APIUrlCommit"+ str(i+1) +".txt \"http://data.zz.baidu.com/urls?site=www.yangbaicaidy.com&token=KddXxHLpqObuFSWR\"" + "\n")
        
f.close

# curl -H 'Content-Type:text/plain' --data-binary @urls.txt "http://data.zz.baidu.com/urls?site=www.yangbaicaidy.com&token=KddXxHLpqObuFSWR"
# f.write("https://www.yangbaicaidy.com\n")
# f.write("https://www.yangbaicaidy.com/films/400\n")
# f.write("https://www.yangbaicaidy.com/soaps/401\n")
# f.write("https://www.yangbaicaidy.com/superHero/404\n")
# f.write("https://www.yangbaicaidy.com/doubanTop/405\n")
# f.write("https://www.yangbaicaidy.com/TVshows/402\n")
# f.write("https://www.yangbaicaidy.com/cartoons/403\n")
