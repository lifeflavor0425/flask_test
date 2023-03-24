"""
    데이터베이스 접속 후 쿼리 실행
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
        sql = "select uid,`name`, regdate from users where uid='guest' AND upw='1234';"
        cursor.execute(sql)
        row = cursor.fetchone()
        print(row.get("name"))

except Exception as e:
    print("접속 오류", e)
else:
    print("문제 없음")
finally:
    if connection:
        connection.close()
