from flask import Flask, render_template, request, redirect, url_for
import pymysql
import getpass
import query as q
import rec_conn as rdb

app = Flask(__name__)

# DB 연결 함수 (rec_conn.py에 정의된 내용 참고)
def mysql_rdb_conn():
    conn = pymysql.connect(
        host="localhost",  # 호스트 주소
        user="root",       # MySQL 사용자 이름
        password="1234",   # MySQL 비밀번호
        database="RECIPE",  # 데이터베이스 이름
        port=3306          # 포트 번호 (기본 MySQL 포트)
    )
    return conn

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # 아이디, 닉네임, 이메일, 비밀번호 받기
        user_id = "asdf"
        nickname = request.form['nickname']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm-password']

        try:
            # MySQL 연결
            conn = mysql_rdb_conn()
            curs = conn.cursor()

            # 아이디 중복 체크
            curs.execute(q.select_user_id_from_users(), (user_id,))
            if curs.fetchone():
                return "이미 사용 중인 아이디입니다."

            # 닉네임 중복 체크
            curs.execute(q.select_nickname_from_users(), (nickname,))
            if curs.fetchone():
                return "이미 사용 중인 닉네임입니다."

            # 이메일 유효성 체크
            if "@" not in email:
                return "올바른 이메일 형식을 입력해주세요."

            # 비밀번호 일치 체크
            if password != confirm_password:
                return "비밀번호가 일치하지 않습니다."

            # 회원가입 정보 DB에 삽입
            regi_data = (user_id, nickname, email, password)
            curs.execute(q.mem_register(), regi_data)
            conn.commit()

            return redirect(url_for('home'))  # 회원가입 성공 후 홈으로 리다이렉트

        except Exception as e:
            return f"Unexpected error: {e}"

        finally:
            conn.close()

    return render_template('home')

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
