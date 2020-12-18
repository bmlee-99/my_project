from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 설치 먼저 해야겠죠?)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db 를 사용합니다.(이름을 마음대로 만들수 있다)'dbsparta' db가 없다면 새로 만듭니다.
# 데이터 베이스까지 접근함
# MongoDB에 insert 하기

# # 'users'라는 collection에 데이터를 생성합니다.
# db.users.insert_one({'name': '덤블도어', 'age': 116})
# # users 라는 컬랙션에 insert_one는 document 하나를 집어 넣겠다->몽고디비의 디비스르타안에 들어가있다.
# db.users.insert_one({'name': '맥고나걸', 'age': 85})
# db.users.insert_one({'name': '스네이프', 'age': 60})
# db.users.insert_one({'name': '해리', 'age': 40})
# db.users.insert_one({'name': '허마이오니', 'age': 40})
# db.users.insert_one({'name': '론', 'age': 40})
# # 이코드의 의해서 몽고디비에 저장이 됬다
# user = find_one 하나만 가지고 옴
all_users = list(db.users.find({ 'age': 40}, {'_id': False}))
# list 로 감싸지 않았을때 curser 는 정보가 너무 많다라는 가정을 하여, 데이터베이스의 위치만 next 같은 것만 반환을 해줌
# find 뒤에 이름등 원하는 것만 빼낼수 있다, _id는 몽고에서 임의로 만드는것, 두번째에 넣어놔야함
for user in all_users:
    print