
import time
from sql.sqlconnection import db
db_cur = db.cursor()

db_cur.execute("select filmsId from films order by filmsId;")
filmMsg = db_cur.fetchall()
f=open("sitemap.txt","a")
f.write("https://www.yangbaicaidy.com\n")
f.write("https://www.yangbaicaidy.com/films/400\n")
f.write("https://www.yangbaicaidy.com/soaps/401\n")
f.write("https://www.yangbaicaidy.com/superHero/404\n")
f.write("https://www.yangbaicaidy.com/doubanTop/405\n")
f.write("https://www.yangbaicaidy.com/TVshows/402\n")
f.write("https://www.yangbaicaidy.com/cartoons/403\n")
for v in filmMsg :
    url = 'https://www.yangbaicaidy.com/detail/' + str(v[0]) + '\n'
    f.write(url)
f.close
