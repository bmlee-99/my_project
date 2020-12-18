from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

## 코딩 할 준비 ##

target_movie = db.movies.find_one({'title' : '월-E'})
target_star = target_movie['star']
# same_movies = list(db.movies.find({'star': target_star})) #target_star 가 월E의 평점
# for same_movie in same_movies:
#     print(same_movie['title'])
#       db.movies.update_one(same_movie,{'$set': {'star': '0'}} ) <-이렇게 할수도 있음, 성능상 떨어짐

db.movies.update_many({'star': target_star}, {'$set': {'star': '0'}})
