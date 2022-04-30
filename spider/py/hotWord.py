
import time
import re
from sql.sqlconnection import db
db_cur = db.cursor()
page = str(0 * 1000)
db_cur.execute("select filmsName from films order by filmsId desc limit 759;")
# db_cur.execute("select filmsName from films order by filmsId desc limit "+ page +",1000;")
filmMsg = db_cur.fetchall()
filmsNameStr = ""
for v in filmMsg:
    searchObj = re.search(r'杀手|习|彩世界|越狱|步枪|克隆|禁书|消防队|团派|弩',v[0])
    if bool(searchObj) == False:
        filmsNameStr = filmsNameStr + "," + v[0]

f=open("filmsNameStr.txt","w")
f.write(filmsNameStr.strip(','))
f.close
