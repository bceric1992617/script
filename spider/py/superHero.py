
import time
from sql.sqlconnection import db
db_cur = db.cursor()

marvelArr = [
    '神奇四侠',
    '神奇四侠2',
    '新神奇四侠2015',
    '奇异博士',
    '雷神',    #没有
    '雷神2黑暗世界',
    '雷神索尔3：诸神的黄昏',
    '神奇四侠2',
    '神奇四侠2',
    '蜘蛛侠1',
    '蜘蛛侠2',
    '蜘蛛侠3',
    '超凡蜘蛛侠',
    '超凡蜘蛛侠2',
    '蜘蛛侠：英雄归来',
    '蜘蛛侠：英雄远征',
    '毒液',
    '美国队长',
    '美国队长2',
    '美国队长3',
    '钢铁侠',
    '钢铁侠2',
    '钢铁侠3',
    '复仇者联盟',
    '复仇者联盟2',
    '复仇者联盟3无限战争',
    '复仇者联盟4：终局之战',
    '银河护卫队',
    '银河护卫队2',
    '黑豹',
    '蚁人',
    '蚁人2黄蜂女现身',
    '金刚狼',
    '金刚狼2',
    '金刚狼3',
    '死侍',
    '死侍2',
    '刀锋战士',
    '刀锋战士2',
    '刀锋战士3',
    '艾丽卡',
    '惩罚者',
    '惩罚者2:战争特区',
    '灵魂战车',
    '灵魂战车2:复仇时刻'
    'X战警：黑凤凰',
    'X战警：新变种人',
    'X战警：第一战',
    'X战警：逆转未来',
    'X战警变种特攻',
    'X战警3：背水一战',
    'X战警2变种特攻2',
    'X战警天启',
    'X战警3背水一战',
]

DCArr = [
    '超人和鼹鼠人',
    '蝙蝠侠：电影',
    '神奇女侠',
    '超人',
    '超人2',
    '沼泽怪物',
    '超人3',
    '女超人',
    '超人4',
    '沼泽怪物归来',
    '蝙蝠侠',
    '蝙蝠侠归来',
    '蝙蝠侠大战幻影人',
    '永远的蝙蝠侠',
    '美国正义联盟',
    '蝙蝠侠与罗宾',
    '钢人',
    '猫女',
    '康斯坦丁',
    'V字仇杀队',
    '蝙蝠侠：侠影之谜',
    '超人归来',
    '黑暗骑士',
    '守望者',
    '失败者',
    '西部英雄约拿·哈克斯',
    '绿灯侠',
    '黑暗骑士崛起',
    '乐高蝙蝠侠大电影',
    '小丑',
    '超人：钢铁之躯',
    'DC电影出品：正义联盟黎明 ',
    '蝙蝠侠大战超人：正义黎明',
    '自杀小队',
    '正义联盟',
    '海王',
    '雷霆沙赞',
    '猛禽小队',
    '神奇女侠1984',
    '特种部队：蛇眼起源 ',
    '海沟族',
    '海王2',
    '自杀小队',
    '自杀小队2',
    '黑亚当',
    '绿灯军团',
]

for v in DCArr:
    insertSql = 'insert into superHero(filmsId,filmsName,types,createTime,updateTime,isDel) values(%s,%s,%s,%s,%s,%s)'
    db_cur.execute("select filmsId from films where filmsName= '"+ v +"' limit 1;")
    filmMsg = db_cur.fetchone()
    if bool(filmMsg) :
        db_cur.execute(insertSql, [
            filmMsg,
            v,
            2,
            int(round(time.time())),
            int(round(time.time())),
            0            
        ])

for v in marvelArr:
    db_cur.execute("select filmsId from films where filmsName= '"+ v +"' limit 1;")
    insertSql = 'insert into superHero(filmsId,filmsName,types,createTime,updateTime,isDel) values(%s,%s,%s,%s,%s,%s)'
    filmMsg = db_cur.fetchone()
    if bool(filmMsg) :
        db_cur.execute(insertSql, [
            filmMsg,
            v,
            1,
            int(round(time.time())),
            int(round(time.time())),
            0            
        ])
db.commit() 