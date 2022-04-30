import pymysql 
db = pymysql.connect(
    host="localhost",
    port=3306, 
    db='cash', 
    user='root', 
    passwd='123321', 
    charset='utf8'
)

