# 나홀로 메모장에 있을것(버튼눌렀을 때 원하는것만 가져오기) 23번
# 4주차 서버를 띄우는거임
from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

app = Flask(__name__)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 만들거나 사용합니다.


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/memo', methods=['GET'])
def read_articles():
    # 1. mongoDB에서 _id 값을 제외한 모든 데이터 조회해오기 (Read)
    regionCd_receive = request.args.get('regionCd')
    print(regionCd_receive)

    result = list(db.river.find({'regionCd':regionCd_receive}, {'_id': 0}))
    print(result)

    # 2. articles라는 키 값으로 article 정보 보내주기
    return jsonify({'result': 'success', 'articles': result})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)

    # 서버를 html불러와서 띄움
# IF~ 는 맨 뒷쪽에 와아ㅑ함 규칙  __NAME__같은게 뒤에있어야 에러날 확률낮아짐
