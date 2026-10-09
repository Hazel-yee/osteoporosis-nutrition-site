# -*- codeing = ansi -*-
# @Time : 2022/2/26 19:41
# @Author : Yi
# @File : spider.py
# @Software : PyCharm
import urllib.request
from bs4 import BeautifulSoup
import re
import sqlite3



findTitle = re.compile(r'<b>(.*)</b>')
findG = re.compile(r'<div class="list"><div class="list_m">钙\(毫克\)</div>(.*?)</div>')
findZ = re.compile(r'<div class="list"><div class="list_m">脂肪\(克\)</div>(.*?)</div>')
findL = re.compile(r'<div class="list"><div class="list_m">磷\(毫克\)</div>(.*?)</div>')


def main48():
    # 爬取类别：畜肉类
    baseurl = ["目标网页链接".format(str(i)) for i in range(0, 页数)]  # 填入该类列表页链接（含{}占位）与页数
    datalist = getDATA(baseurl)
    dbpath = "Chu_GZL.db"  # 库名为按论文命名规律
    saveData2(datalist, dbpath)


# 1.爬取网页
def getDATA(baseurl):
    datalist = []
    for every in baseurl:
        url = every
        html = askURL(url)
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all('div', id="rightlist"):
            data = []
            item = str(item)
            title = re.findall(findTitle, item)[0]
            data.append(title)
            dn = re.findall(findG, item)[0]
            data.append(dn)
            dn = re.findall(findZ, item)[0]
            data.append(dn)
            dn = re.findall(findL, item)[0]
            data.append(dn)
            datalist.append(data)
    return datalist


# 得到指定一个url的网页内容
def askURL(url):
    head = {
        "User-Agent": "Mozilla "
                      "/ 5.0(Windows NT 10.0;WOW64) AppleWebKit "
                      "/ 537.36(KHTML, like Gecko) Chrome "
                      "/ 84.0.4147.89 Safari "
                      "/ 537.36 SLBrowser "
                      "/ 7.0.0.12151 SLBChan / 23"
    }

    request = urllib.request.Request(url, headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("ansi")
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html



# 保存数据
def saveData2(datalist, dbpath):
    init_db(dbpath)
    conn = sqlite3.connect(dbpath)
    cur = conn.cursor()
    for data in datalist:
        for index in range(len(data)):
            data[index] = '"' + data[index] + '"'
        sql = '''
              insert into Gdbz(
              name,scoreG,scoreZ,scoreL)
              values(%s)''' % ",".join(data)
        print(sql)
        cur.execute(sql)
        conn.commit()
    cur.close()
    conn.close()


def init_db(dbpath):
    sql = '''
          create table Gdbz
          (
          name varchar,
          scoreG numeric,
          scoreZ numeric,
          scoreL numeric
          )
    '''
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()


if __name__ == "__main__":
    main48()
