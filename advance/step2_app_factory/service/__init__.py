# 사용자가 정의한(커스텀) 엔트리 포인트
from flask import Flask

"""
    create_app은 플라스크 내부에서 정의된 함수명(수정 x)
    flask run을 수행하면 내부적으로 엔트리포인트 모듈에서 create_app()를 찾는다
    차후, 다른 모듈에서는 flask.current_app 이라는 변수로 app을 접근할 수 있다
"""


def create_app():
    app = Flask(__name__)
    # 환경 변수 초기화
    init_environment(app)
    # 데이터 베이스 초기화
    init_database(app)
    # 블루프린트 초기화
    init_blueprint(app)
    return app


def init_database(app):
    # pool
    from .model import pool_sql

    pool_sql.init_pool()
    # 테스트
    print(pool_sql.login("guest", "1234"))


def init_environment(app):
    # 특정파일(cfg, ...)등을 읽어서 처리 가능
    app.config.from_pyfile("./resource/config.cfg", silent=True)

    from . import config as config

    # py를 모듈가져오기 해서(객체)를 세팅해서 처리
    app.config.from_object(config)
    # 환경변수(os레벨, 플라스크레벨, 사용자정의 레벨) 모두 출력
    print("\n" + "-" * 20)
    # 개별 환경 변수값 추출
    print(app.config["SECRET_KEY"])
    # for k, v in app.config.items():
    #     print(k, v)
    print("-" * 20 + "\n")


def init_blueprint(app):
    # app 에 블루프린트 객체를 등록한다.

    # 블루프린트로 정의된 개별 페이지 관련 내용 로드
    from .controlers import main_controler, auth_controler

    # 이 위치에서는 service를 생략하고 표현 가능
    # from service.controlers import bp_main
    from .controlers import bp_main, bp_auth

    # 플라스크 객체에 블루 프린트 등록
    app.register_blueprint(bp_main)
    app.register_blueprint(bp_auth)
