
import time
import re
from sql.sqlconnection import db
db_cur = db.cursor()

db_cur.execute("select filmsName from hot order by filmsId desc limit 110;")
filmMsg = db_cur.fetchall()

filmsNameStr = ""
for v in filmMsg:
    searchObj = re.search(r'杀手|习|彩世界|越狱|步枪|克隆|禁书|消防队|团派|弩|窃听|大烟|子弹|恐怖直播|去死|革命|杀人|杀人事件|自杀|死了|爆炸',v[0])
    if bool(searchObj) == False:
        filmsNameStr = filmsNameStr + "," + v[0]

f=open("hotVideoWord.txt","w")
f.write(filmsNameStr.strip(','))
f.close
