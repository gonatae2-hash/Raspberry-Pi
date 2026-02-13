from flask import Flask, jsonify, request

app = Flask(__name__)
app.users = {}
app.id_count = 1 # new_user 등록시 카운트
app.tweets=[]

@app.route('/sign_up', methods=['POST'])# POST = 데이터 새로 생성시
def sign_up():
    new_user = request.json             # name=kim 입력 시 request.json 객체에 들어감.
                                        # new_user 변수에 대입.
    new_user["id"] = app.id_count       # new_user 딕셔너리에 id 추가.
                                        # 그 값으로 app.id_count(1)를 넣음.
    app.users[app.id_count] = new_user  # id를 기준으로 유저 정보 저장.
    app.id_count = app.id_count + 1     # 새로운 유저를 위해 1씩 증가.
    return jsonify(new_user)            # name=kim 입력 시 id, name 출력.

@app.route('/user/<int:user_id>', methods=['GET']) # GET = 저장된 데이터 조회
def user(user_id):
    if user_id not in app.users:
        return '사용자가 존재하지 않습니다.', 400
    
    return jsonify(app.users[user_id])

# 전체 유저 조회
@app.route('/users', methods=['GET'])
def users():
    result = []
    
    for user in app.users.values(): #.values() 딕셔너리 안의 값만 가져옴.
        remvpw_user = {key : value for key, value in user.items() if key != "password"}
        # {만들형태  for 꺼낼값 in 반복대상  if 조건}
        # password가 아닐 시 user.items()에서 key, value를 key : velue형태로
        # remvpw_user 딕셔너리에 추가(user 한명씩 추가)
        result.append(remvpw_user) # remvpw_user를 result리스트에 추가.
    return result
                              
@app.route('/tweet', methods=['POST'])
def tweet():
    payload = request.json      # tweet = 안녕 입력 시 request.json 객체에 들어감.
                                # payload 변수에 대입.
    user_id=int(payload['id'])  # id = 1입력시 "1"문자열로 들어옴 int로 정수변환
    tweet = payload['tweet']

    if user_id not in app.users:
        return '사용자가 존재하지 않습니다.', 400

    if len(tweet) > 300:
        return '300자를 초과했습니다.', 400
    
    app.tweets.append({
        'user_id' : user_id,
        'tweet'   : tweet
    })

    return jsonify(app.tweets), 200