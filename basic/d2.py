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
        # 조회 결과는 [{}, {}, {} ...] 이런 형태로 추출된다.
        cursorclass=my.cursors.DictCursor,
    )
    # 쿼리 수행
    # pymysql은 커서를 획득해서 쿼리를 수행한다. -> Rule
    # 1. 커서 획득
    # connection.cursor(my.cursors.DictCursor)
    with connection.cursor() as cursor:
        # 2. sql문 준비
        sql = "select uid,`name`, regdate from users where uid='guest' AND upw='1234';"
        # 3. sql쿼리 수행
        cursor.execute(sql)
        # 4. 결과를 획득
        row = cursor.fetchone()
        # 5. 결과 확인
        print(row.get("uid"))

except Exception as e:
    print("접속 오류", e)
else:
    print("문제 없음")
finally:
    if connection:
        connection.close()
