"""
    파이썬 <-> 데이터베이스
    파이썬으로 데이터베이스를 엑세스하여, 쿼리를 전송, 수행결과를 받아오는 방식
        - sql 수행
            - basic에서 수행
            - pymysql 패키지 사용
        - orm 수행
            - advance에서 수행
    업무 포지션은, 지원팀, 공용 API를 만드는 파트 => 함수, 클래스 형태로 라이브러리 제공
    사용방법에 대한 예제까지 제공
    
    데이터베이스를 터미널 통해서 접속
    1. root 권한으로 접속
        $ mysql -u root -p
        -> password : ********
    2. 데이터베이스 생성
        create database [이름] ;
    3. 데이터베이스 목록 출력(보여줘)
        show databases ;
        +--------------------+
        | Database           |
        +--------------------+
        | information_schema |
        | ml_db              |
        | mysql              |
        | news_data_db       |
        | performance_schema |
        | sys                |
        +--------------------+
    4. 현재 작업(사용)할 데이터베이스 지정
        use ml_db ; 
    5. 고객 테이블 생성
    CREATE TABLE `users` (
        `id` INT(11) NOT NULL AUTO_INCREMENT COMMENT '고객 고유 ID',
        `uid` VARCHAR(32) NOT NULL COMMENT '고객 로그인 아이디' COLLATE 'utf8mb4_general_ci',
        `upw` VARCHAR(128) NOT NULL COMMENT '고객 로그인 비번' COLLATE 'utf8mb4_general_ci',
        `name` VARCHAR(32) NOT NULL COMMENT '고객 이름' COLLATE 'utf8mb4_general_ci',
        `regdate` TIMESTAMP NOT NULL COMMENT '고객 가입일',
        PRIMARY KEY (`id`) USING BTREE,
        UNIQUE INDEX `uid` (`uid`) USING BTREE
    )
    COMMENT='고객 테이블'
    COLLATE='utf8mb4_general_ci'
    ENGINE=InnoDB
    ;
    +---------+--------------+------+-----+---------+----------------+
    | Field   | Type         | Null | Key | Default | Extra          |
    +---------+--------------+------+-----+---------+----------------+
    | id      | int(11)      | NO   | PRI | NULL    | auto_increment |
    | uid     | varchar(32)  | NO   | UNI | NULL    |                |
    | upw     | varchar(128) | NO   |     | NULL    |                |
    | name    | varchar(32)  | NO   |     | NULL    |                |
    | regdate | timestamp    | NO   |     | NULL    |                |
    +---------+--------------+------+-----+---------+----------------+
    5-1 스키마 수정
    ALTER TABLE `users`
	CHANGE COLUMN `name` `name` VARCHAR(32) NOT NULL COMMENT '고객 이름' COLLATE 'utf8mb4_general_ci' AFTER `upw`,
	CHANGE COLUMN `regdate` `regdate` TIMESTAMP NOT NULL COMMENT '고객 가입일' AFTER `name`;
    6. 회원가입 -> insert
        - insert into users () values ();
        - ex) 
            Insert into
                users
                (`uid`,`upw`,`name`,`regdate`)
            values
                ('guest','1234','게스트', now());
                
    7. 로그인 -> select
        - select * from (table)
        - 대소문자 구분 안한다.
        
    8. 회원 정보 수정 -> update
    
    9. 회원 탈퇴 -> delete
        - 1년간 보관?, 완전 삭제?
"""
"""
    파이썬에서 DB에 접속, 접속해제
"""
import pymysql as my

connection = None
# 1. 접속
try:
    connection = my.connect(
        host="localhost",  # 127.0.0.1
        # port=3306,                          # 포트
        user="root",  # 사용자 계정,  root 게정 아닌것 사용 권장
        password="12341234",  # 비밀번호
        database="ml_db",  # 접속할 db
        # cursorclass=my.cursors.DictCursor
    )
except Exception as e:
    print("접속 오류", e)
else:
    print("접속 ")
finally:
    # 2. 접속 종료(I/O) -> close()
    if connection:
        connection.close()
        print("접속 종료")
