"""
    데이터베이스 접속 후 쿼리 실행 + 
"""
import pymysql as my

connection = None
try:
    connection = my.connect(
        host="localhost",
        # port=3306,
        user="root",
        password="12341234",
        database="ml_db",
        cursorclass=my.cursors.DictCursor,
    )
    with connection.cursor() as cursor:  # cursor는 with문을 벗어나면 자동으로 닫힘
        # 파라미터는 %s 표시로 순서대로 세팅된다 '값' => ''는 자동으로  세팅된다.
        sql = "select uid,`name`, regdate from users where uid=%s AND upw=%s;"
        # excute() 함수의 2번 인자가 파라미터 전달하는 자리, 튜플로 표현
        cursor.execute(sql, ("guest", "1234"))
        row = cursor.fetchone()
        print(row.get("name"))

except Exception as e:
    print("접속 오류", e)
else:
    print("문제 없음")
finally:
    if connection:
        connection.close()
