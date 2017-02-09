# -- coding: utf-8 --
#처리된 데이터를 json형식으로 리턴해주기위해 사용
import json
#python mysql 연결 드라이버
import pymysql

#db연결을 담당할 함스
def getConnection():
    return pymysql.connect(host='localhost', user='root', password='123456',
                           db='myintranet', charset='utf8')

#select한 데이터중 mysql datetime형식의 값을 fullCalendar에서 처리할수 있도록 포멧 변경
def date_handler(obj):
    return obj.isoformat() if hasattr(obj, 'isoformat') else obj

#등록된 schedule을 가져옴
def getScheduler(searchDate):
    # Connection 연결
    conn = getConnection()

    # select한 데이터를 Dictoionary 형태로 가져옴
    curs = conn.cursor(pymysql.cursors.DictCursor)

    # SQL 처리
    sql = "select id, title, start, end, if(allDay = %s,true,false) allDay from my_schedule where to_days(start) >= to_days(%s) and to_days(end) <= to_days(%s)"
    curs.execute(sql, ('Y', searchDate['start'], searchDate['end']))

    # 처리된 data 가져옴
    rows = curs.fetchall()

    # Connection 닫기
    conn.close()

    #처리된 데이터를 json으로 변경 datetime처리를 위해 date_handler지정
    return json.dumps(rows, default=date_handler);

#넘어온 schedule을 등록
def setScheduler(schedule):
    # connetion 가져옴
    conn = getConnection()
    # cursor 생성
    cur = conn.cursor()
    # 데이터 입력
    ok = cur.execute("INSERT INTO my_schedule(title, start, end, allDay) VALUES (%s, now(), now(), 'Y')",(schedule['title']))
    # commit
    conn.commit()
    # Connection 닫기
    conn.close()
    # 처리 결과를 json형식으로 리턴
    return json.dumps({'rows' : ok})
