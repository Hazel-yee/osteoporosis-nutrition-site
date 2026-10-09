import sqlite3
from flask import Flask, render_template

app = Flask(__name__)


# 主页面
@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')


# 二级页面
@app.route('/Cal')
def Cal():
    name = []
    scoreG = []
    scoreZ = []
    scoreL = []
    # 累积添加
    name42, scoreG42, scoreZ42, scoreL42 = Cal42()
    name43, scoreG43, scoreZ43, scoreL43 = Cal43()
    name44, scoreG44, scoreZ44, scoreL44 = Cal44()
    name45, scoreG45, scoreZ45, scoreL45 = Cal45()
    name46, scoreG46, scoreZ46, scoreL46 = Cal46()
    name47, scoreG47, scoreZ47, scoreL47 = Cal47()
    name48, scoreG48, scoreZ48, scoreL48 = Cal48()
    name49, scoreG49, scoreZ49, scoreL49 = Cal49()
    name410, scoreG410, scoreZ410, scoreL410 = Cal410()
    name411, scoreG411, scoreZ411, scoreL411 = Cal411()
    name412, scoreG412, scoreZ412, scoreL412 = Cal412()
    name413, scoreG413, scoreZ413, scoreL413 = Cal413()
    name414, scoreG414, scoreZ414, scoreL414 = Cal414()
    name415, scoreG415, scoreZ415, scoreL415 = Cal415()
    name416, scoreG416, scoreZ416, scoreL416 = Cal416()
    name417, scoreG417, scoreZ417, scoreL417 = Cal417()
    con = sqlite3.connect("Gu_GZL.db")  # 谷类（编号41）
    cur = con.cursor()
    sql = "select * from Gdbz"
    data = cur.execute(sql)
    for item in data:
        name.append(item[0])
        scoreG.append(item[1])
        scoreZ.append(item[2])
        scoreL.append(item[3])
    cur.close()
    con.close()
    return render_template('Cal.html', name=name, scoreG=scoreG, scoreZ=scoreZ, scoreL=scoreL,
                             name42=name42, scoreG42=scoreG42, scoreZ42=scoreZ42, scoreL42=scoreL42,
                             name43=name43, scoreG43=scoreG43, scoreZ43=scoreZ43, scoreL43=scoreL43,
                             name44=name44, scoreG44=scoreG44, scoreZ44=scoreZ44, scoreL44=scoreL44,
                             name45=name45, scoreG45=scoreG45, scoreZ45=scoreZ45, scoreL45=scoreL45,
                             name46=name46, scoreG46=scoreG46, scoreZ46=scoreZ46, scoreL46=scoreL46,
                             name47=name47, scoreG47=scoreG47, scoreZ47=scoreZ47, scoreL47=scoreL47,
                             name48=name48, scoreG48=scoreG48, scoreZ48=scoreZ48, scoreL48=scoreL48,
                             name49=name49, scoreG49=scoreG49, scoreZ49=scoreZ49, scoreL49=scoreL49,
                             name410=name410, scoreG410=scoreG410, scoreZ410=scoreZ410, scoreL410=scoreL410,
                             name411=name411, scoreG411=scoreG411, scoreZ411=scoreZ411, scoreL411=scoreL411,
                             name412=name412, scoreG412=scoreG412, scoreZ412=scoreZ412, scoreL412=scoreL412,
                             name413=name413, scoreG413=scoreG413, scoreZ413=scoreZ413, scoreL413=scoreL413,
                             name414=name414, scoreG414=scoreG414, scoreZ414=scoreZ414, scoreL414=scoreL414,
                             name415=name415, scoreG415=scoreG415, scoreZ415=scoreZ415, scoreL415=scoreL415,
                             name416=name416, scoreG416=scoreG416, scoreZ416=scoreZ416, scoreL416=scoreL416,
                             name417=name417, scoreG417=scoreG417, scoreZ417=scoreZ417, scoreL417=scoreL417)


# 以下 Cal42()~Cal417() 分别读取 16 个食材类别的钙/脂肪/磷数据库，
# 编号与 spiders/GZL 目录下爬虫的 main 编号一一对应（41=谷类 在上方 Cal() 中直接读取）。

def Cal42():
    name = []
    scoreG = []
    scoreZ = []
    scoreL = []
    con = sqlite3.connect("Shu_GZL.db")  # 薯类淀粉
    cur = con.cursor()
    sql = "select * from Gdbz"
    data = cur.execute(sql)
    for item in data:
        name.append(item[0])
        scoreG.append(item[1])
        scoreZ.append(item[2])
        scoreL.append(item[3])
    cur.close()
    con.close()
    return name, scoreG, scoreZ, scoreL

def Cal43():
    name = []
    scoreG = []
    scoreZ = []
    scoreL = []
    con = sqlite3.connect("GanDou_GZL.db")  # 干豆类
    cur = con.cursor()
    sql = "select * from Gdbz"
    data = cur.execute(sql)
    for item in data:
        name.append(item[0])
        scoreG.append(item[1])
        scoreZ.append(item[2])
        scoreL.append(item[3])
    cur.close()
    con.close()
    return name, scoreG, scoreZ, scoreL

def Cal44():
    name = []
    scoreG = []
    scoreZ = []
    scoreL = []
    con = sqlite3.connect("ShuCai_GZL.db")  # 蔬菜类
    cur = con.cursor()
    sql = "select * from Gdbz"
    data = cur.execute(sql)
    for item in data:
        name.append(item[0])
        scoreG.append(item[1])
        scoreZ.append(item[2])
        scoreL.append(item[3])
    cur.close()
    con.close()
    return name, scoreG, scoreZ, scoreL

def Cal45():
    name = []
    scoreG = []
    scoreZ = []
    scoreL = []
    con = sqlite3.connect("JunZao_GZL.db")  # 菌藻类
    cur = con.cursor()
    sql = "select * from Gdbz"
    data = cur.execute(sql)
    for item in data:
        name.append(item[0])
        scoreG.append(item[1])
        scoreZ.append(item[2])
        scoreL.append(item[3])
    cur.close()
    con.close()
    return name, scoreG, scoreZ, scoreL

def Cal46():
    name = []
    scoreG = []
    scoreZ = []
    scoreL = []
    con = sqlite3.connect("ShuiGuo_GZL.db")  # 水果类
    cur = con.cursor()
    sql = "select * from Gdbz"
    data = cur.execute(sql)
    for item in data:
        name.append(item[0])
        scoreG.append(item[1])
        scoreZ.append(item[2])
        scoreL.append(item[3])
    cur.close()
    con.close()
    return name, scoreG, scoreZ, scoreL

def Cal47():
    name = []
    scoreG = []
    scoreZ = []
    scoreL = []
    con = sqlite3.connect("JianGuo_GZL.db")  # 坚果种子
    cur = con.cursor()
    sql = "select * from Gdbz"
    data = cur.execute(sql)
    for item in data:
        name.append(item[0])
        scoreG.append(item[1])
        scoreZ.append(item[2])
        scoreL.append(item[3])
    cur.close()
    con.close()
    return name, scoreG, scoreZ, scoreL

def Cal48():
    name = []
    scoreG = []
    scoreZ = []
    scoreL = []
    con = sqlite3.connect("Chu_GZL.db")  # 畜肉类
    cur = con.cursor()
    sql = "select * from Gdbz"
    data = cur.execute(sql)
    for item in data:
        name.append(item[0])
        scoreG.append(item[1])
        scoreZ.append(item[2])
        scoreL.append(item[3])
    cur.close()
    con.close()
    return name, scoreG, scoreZ, scoreL

def Cal49():
    name = []
    scoreG = []
    scoreZ = []
    scoreL = []
    con = sqlite3.connect("Qin_GZL.db")  # 禽肉类
    cur = con.cursor()
    sql = "select * from Gdbz"
    data = cur.execute(sql)
    for item in data:
        name.append(item[0])
        scoreG.append(item[1])
        scoreZ.append(item[2])
        scoreL.append(item[3])
    cur.close()
    con.close()
    return name, scoreG, scoreZ, scoreL

def Cal410():
    name = []
    scoreG = []
    scoreZ = []
    scoreL = []
    con = sqlite3.connect("Ru_GZL.db")  # 乳类
    cur = con.cursor()
    sql = "select * from Gdbz"
    data = cur.execute(sql)
    for item in data:
        name.append(item[0])
        scoreG.append(item[1])
        scoreZ.append(item[2])
        scoreL.append(item[3])
    cur.close()
    con.close()
    return name, scoreG, scoreZ, scoreL

def Cal411():
    name = []
    scoreG = []
    scoreZ = []
    scoreL = []
    con = sqlite3.connect("Dan_GZL.db")  # 蛋类
    cur = con.cursor()
    sql = "select * from Gdbz"
    data = cur.execute(sql)
    for item in data:
        name.append(item[0])
        scoreG.append(item[1])
        scoreZ.append(item[2])
        scoreL.append(item[3])
    cur.close()
    con.close()
    return name, scoreG, scoreZ, scoreL

def Cal412():
    name = []
    scoreG = []
    scoreZ = []
    scoreL = []
    con = sqlite3.connect("SuShi_GZL.db")  # 速食食品
    cur = con.cursor()
    sql = "select * from Gdbz"
    data = cur.execute(sql)
    for item in data:
        name.append(item[0])
        scoreG.append(item[1])
        scoreZ.append(item[2])
        scoreL.append(item[3])
    cur.close()
    con.close()
    return name, scoreG, scoreZ, scoreL

def Cal413():
    name = []
    scoreG = []
    scoreZ = []
    scoreL = []
    con = sqlite3.connect("Ruan_GZL.db")  # 软饮料
    cur = con.cursor()
    sql = "select * from Gdbz"
    data = cur.execute(sql)
    for item in data:
        name.append(item[0])
        scoreG.append(item[1])
        scoreZ.append(item[2])
        scoreL.append(item[3])
    cur.close()
    con.close()
    return name, scoreG, scoreZ, scoreL

def Cal414():
    name = []
    scoreG = []
    scoreZ = []
    scoreL = []
    con = sqlite3.connect("Jiu_GZL.db")  # 酒精饮料
    cur = con.cursor()
    sql = "select * from Gdbz"
    data = cur.execute(sql)
    for item in data:
        name.append(item[0])
        scoreG.append(item[1])
        scoreZ.append(item[2])
        scoreL.append(item[3])
    cur.close()
    con.close()
    return name, scoreG, scoreZ, scoreL

def Cal415():
    name = []
    scoreG = []
    scoreZ = []
    scoreL = []
    con = sqlite3.connect("Tang_GZL.db")  # 糖蜜饯类
    cur = con.cursor()
    sql = "select * from Gdbz"
    data = cur.execute(sql)
    for item in data:
        name.append(item[0])
        scoreG.append(item[1])
        scoreZ.append(item[2])
        scoreL.append(item[3])
    cur.close()
    con.close()
    return name, scoreG, scoreZ, scoreL

def Cal416():
    name = []
    scoreG = []
    scoreZ = []
    scoreL = []
    con = sqlite3.connect("You_GZL.db")  # 油脂类
    cur = con.cursor()
    sql = "select * from Gdbz"
    data = cur.execute(sql)
    for item in data:
        name.append(item[0])
        scoreG.append(item[1])
        scoreZ.append(item[2])
        scoreL.append(item[3])
    cur.close()
    con.close()
    return name, scoreG, scoreZ, scoreL

def Cal417():
    name = []
    scoreG = []
    scoreZ = []
    scoreL = []
    con = sqlite3.connect("Tiao_GZL.db")  # 调味品类
    cur = con.cursor()
    sql = "select * from Gdbz"
    data = cur.execute(sql)
    for item in data:
        name.append(item[0])
        scoreG.append(item[1])
        scoreZ.append(item[2])
        scoreL.append(item[3])
    cur.close()
    con.close()
    return name, scoreG, scoreZ, scoreL


@app.route('/Pro')
def Pro():
    name = []
    score = []
    # 累积添加
    name03, score03 = Pro03()
    name010, score010 = Pro010()
    name08, score08 = Pro08()
    name09, score09 = Pro09()
    name011, score011 = Pro011()
    con = sqlite3.connect("YingYang.db")
    cur = con.cursor()
    sql = "select * from Gdbz"
    data = cur.execute(sql)
    for item in data:
        name.append(item[0])
        score.append(item[1])
    cur.close()
    con.close()
    return render_template('Pro.html', name=name, score=score,
                             name03=name03, score03=score03,
                             name010=name010, score010=score010,
                             name08=name08, score08=score08,
                             name09=name09, score09=score09,
                             name011=name011, score011=score011)


# 以下 Pro03()~Pro011() 分别读取 5 类优质蛋白质来源的数据库，
# 编号与 spiders/protein 目录下爬虫的 main 编号一一对应。

def Pro03():
    name = []
    score = []
    con = sqlite3.connect("GanDou_Dn.db")  # 干豆类
    cur = con.cursor()
    sql = "select * from Gdbz"
    data = cur.execute(sql)
    for item in data:
        name.append(item[0])
        score.append(item[1])
    cur.close()
    con.close()
    return name, score

def Pro010():
    name = []
    score = []
    con = sqlite3.connect("Ru_Dn.db")  # 乳类
    cur = con.cursor()
    sql = "select * from Gdbz"
    data = cur.execute(sql)
    for item in data:
        name.append(item[0])
        score.append(item[1])
    cur.close()
    con.close()
    return name, score

def Pro08():
    name = []
    score = []
    con = sqlite3.connect("Qin_Dn.db")  # 禽肉类
    cur = con.cursor()
    sql = "select * from Gdbz"
    data = cur.execute(sql)
    for item in data:
        name.append(item[0])
        score.append(item[1])
    cur.close()
    con.close()
    return name, score

def Pro09():
    name = []
    score = []
    con = sqlite3.connect("Chu_Dn.db")  # 畜肉类
    cur = con.cursor()
    sql = "select * from Gdbz"
    data = cur.execute(sql)
    for item in data:
        name.append(item[0])
        score.append(item[1])
    cur.close()
    con.close()
    return name, score

def Pro011():
    name = []
    score = []
    con = sqlite3.connect("Dan_Dn.db")  # 蛋类
    cur = con.cursor()
    sql = "select * from Gdbz"
    data = cur.execute(sql)
    for item in data:
        name.append(item[0])
        score.append(item[1])
    cur.close()
    con.close()
    return name, score


@app.route('/Fat')
def Fat():
    return render_template('Fat.html')


@app.route('/Phos')
def Phos():
    return render_template('Phos.html')


@app.route('/Synth')
def Synth():
    return render_template('Synth.html')


if __name__ == '__main__':
    app.run()
