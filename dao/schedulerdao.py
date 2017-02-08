# -- coding: utf-8 --
import json
import pymysql

def getConnection():
    return pymysql.connect(host='localhost', user='root', password='123456',
                           db='myintranet', charset='utf8')

def date_handler(obj):
    return obj.isoformat() if hasattr(obj, 'isoformat') else obj

def getScheduler(searchDate):
    # MySQL Connection 연결
    conn = getConnection()

    # Connection 으로부터 Dictoionary Cursor 생성
    curs = conn.cursor(pymysql.cursors.DictCursor)

    # SQL문 실행
    sql = "select id, title, start, end, if(allDay = %s,true,false) allDay from my_schedule where to_days(start) >= to_days(%s) and to_days(end) <= to_days(%s)"
    curs.execute(sql, ('Y', searchDate['start'], searchDate['end']))

    # 데이타 Fetch
    rows = curs.fetchall()

    # Connection 닫기
    conn.close()

    return json.dumps(rows, default=date_handler);

def setScheduler(schedule):
    conn = getConnection()
    cur = conn.cursor()
    ok = cur.execute("INSERT INTO my_schedule(title, start, end, allDay) VALUES (%s, now(), now(), 'Y')",(schedule['title']))
    conn.commit()
    conn.close()
    return json.dumps({'rows' : ok})
