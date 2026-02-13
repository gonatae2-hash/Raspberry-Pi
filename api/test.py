from flask import Flask, jsonify, request

app = Flask(__name__)
app.users = {}
app.id_count = 1 # new_user 등록시 카운트

@app.route('/sign_up', methods=['POST'])
def sign_up():
    new_user = request.json             # name=kim 입력 시 request.json 객체에 들어감.
                                        # new_user 변수에 대입.
    new_user["id"] = app.id_count       # new_user 딕셔너리에 id 추가.
                                        # 그 값으로 app.id_count(1)를 넣음.
    app.users[app.id_count] = new_user  # id를 기준으로 유저 정보 저장.
    app.id_count = app.id_count + 1     # 새로운 유저를 위해 1씩 증가.
    return jsonify(new_user)            # ame=kim 입력 시 id, name 출력.

@app.route('/user/<int:user_id>', methods=['GET'])
def user(user_id):
    if user_id not in app.users:
        return '사용자가 존재하지 않습니다.', 400
    
    return jsonify(app.users[user_id])

