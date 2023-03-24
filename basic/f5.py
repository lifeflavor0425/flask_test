"""
    - POST 방식으로 데이터 전송하기
        - 클라이언트(Json, Xml, Text, Form(키=값&키=값 ...), Form-encode, Graphql, Binary)
            - form 전송 (=> Form, Form-encode 형식)
                <form action="http://127.0.0.1:5000/link" method="post" > 
                    <input name="name" value="hello" />
                    <input name="age" value="100" />
                    <input type="submit" value="전송" />
                </form>
            - ajax 가능(jQuery 로 표현), 화면은 현재 화면 유지
                - (Json, Xml, Text, Form(키=값&키=값 ...), Form-encode, Graphql, Binary) 방식 가능
                $.post({
                    url : "http://127.0.0.1:5000/link",
                    data: "name=hello&age=100",
                    success:(res)=>{},
                    error : (err)=>{}
                })
        - 서버
            - post 방식 데이터 추출
            - name = request.form.get('name')
            - age = request.form.get('age')
            
"""
from flask import Flask, render_template, jsonify, request, redirect, url_for, session
from d4 import select_login

app = Flask(__name__)
# 세션을 위해서 시크릿 키 지정
app.secret_key = "al;skdfjalsdj"  # 임의값, 통상 해시값 활용


# 로그인을 하여 세션을 얻은 후 홈페이지를 진행해야 사이트의 내용을 보여주겠다 => 컨셉
@app.route("/")
def home():
    if "uid" not in session:
        # return redirect('/login') # url을 사용할 때는 하드코딩 하지 않는다
        # url_for('사용하고자 하는 URL과 연결된 함수명을 기입')
        return redirect(url_for("login"))
    return "hi"


# 메소드 추가는 => methods=['POST', ...]
@app.route("/login", methods=["POST", "GET"])
def login():
    # method별 분기
    if request.method == "GET":
        return render_template("login.html")
    else:
        # 1. 로그인 정보 획득
        uid = request.form.get("uid")
        upw = request.form.get("upw")  # 암호는 차후에 암호화 해야한다(관리자도 볼수 없다. -> 해싱)
        print(uid, upw)
        # 2. 회원 여부 쿼리
        result = select_login(uid, upw)
        # 3. 회원이면
        if result:
            # 세션 : 클라이언트 정보를 서버가 메모리상에 유지하면서,
            #        클라이언트가 간편하게 웹을 이용할 수 있도록 도움을 줌
            #        단점 : 접속 유저가 많으면 서버측 메모리에 부하가 온다 -> 대체제 필요/대안 필요
            #        JWT를 사용하여 보안(사이트 구성시 인증쪽에서 활용: 차주 진행)
            # 3-1. 세션 생성, 기타 필요한 조치 수행
            session["uid"] = uid
            # 3-2. 서비스 메인 화면으로 이동
            return redirect(url_for("home"))

        # 4. 회원아니면
        else:
            print("회원이 아니다!!!")
            # render_template() => jinja2템플릿 엔진 사용
            # 문법 jinja2를 따라간다
            return render_template("error.html", msg="로그인 실패")
        # 4-1. 적당한 메시지 후 다시 로그인 유도
        return redirect("https://www.naver.com")  # 요청을 다른 URL로 포워딩한다.


if __name__ == "__main__":
    app.run(debug=True)
