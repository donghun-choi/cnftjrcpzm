import pymongo

connect_to = pymongo.MongoClient("localhost",27017) # 로컬에서 열린 몽고디비 연결하기
targetDB = connect_to.new_Db # 몽고디비 안에 내가 원하는 디비 선택
# collection = targetDB.members # 멤버라는 컬렉션에 연결

cho = input('choose_collection')

